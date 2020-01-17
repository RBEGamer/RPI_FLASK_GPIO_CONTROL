# 1
from flask import Flask, redirect, request, jsonify
import json  # FOR THE REST API
import os
import wiringpi
#---- SETUP THE DATABASE -----#
from cloudant.client import Cloudant as CouchDB
DB_IP = "127.0.0.1"
if 'COUCHDB_PORT_5984_TCP_ADDR' in os.environ:
    print("IM RUNNING IN DOCKER")
    DB_IP = os.environ['COUCHDB_PORT_5984_TCP_ADDR']
#CLEAR THE DATABASE
#couch_client = CouchDB('admin', 'admin', url='http://' + DB_IP + ':5984', connect=True)
#log_db = couch_client['logs']
#for document in log_db:
#    document.delete()
#couch_client.disconnect();


#
#---------------------------------------------------------------------

LED_PIN_1 = 7
LED_PIN_2 = 0
BUTTON_YELLOW_PIN = 9
BUTTON_BLUE_PIN = 8


wiringpi.wiringPiSetup()

wiringpi.pinMode(LED_PIN_1,1)
wiringpi.pinMode(LED_PIN_2,1)

wiringpi.pinMode(BUTTON_YELLOW_PIN,0)
wiringpi.pinMode(BUTTON_BLUE_PIN,0)

wiringpi.pullUpDnControl(BUTTON_YELLOW_PIN,2)
wiringpi.pullUpDnControl(BUTTON_BLUE_PIN,2)


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def do_redirect():
    tmp = request
    return redirect('/static/index.html')


@app.route('/api/status')
def do_status():
    status = {}
    status['yellow'] =  not wiringpi.digitalRead(BUTTON_YELLOW_PIN)
    status['blue'] = not wiringpi.digitalRead(BUTTON_BLUE_PIN)

    return jsonify(status)

@app.route('/api/led',methods=['post'])
def do_led():
    tmp = request;

    if request.form['index'] == '1':
        wiringpi.digitalWrite(LED_PIN_1,int(request.form['state']))

    if request.form['index'] == '2':
        wiringpi.digitalWrite(LED_PIN_2,int(request.form['state']))

    couch_client = CouchDB('admin', 'admin', url='http://' + DB_IP + ':5984', connect=True)
    log_db = couch_client['logs']

    doc = log_db.create_document({'action':"Der Benutzer hat die LED " + request.form['index'] + " auf "+request.form['state']+" geändert."})


    couch_client.disconnect()

    return jsonify({'status':'ok'})



@app.route('/api/logs')
def do_logs():
    tmp_log = []

    couch_client = CouchDB('admin', 'admin', url='http://' + DB_IP + ':5984', connect=True)
    log_db = couch_client['logs']

    for doc in log_db:
        tmp_log.append(doc['action'])
    couch_client.disconnect()
    return jsonify(tmp_log)



# 1
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # DO NOT IN PRODUCTION
