# 1
from flask import Flask, redirect, request, jsonify
import json  # FOR THE REST API
import os
#---- SETUP THE DATABASE -----#
#CLEAR THE DATABASE
#couch_client = CouchDB('admin', 'admin', url='http://' + DB_IP + ':5984', connect=True)
#log_db = couch_client['logs']
#for document in log_db:
#    document.delete()
#couch_client.disconnect();


#
#---------------------------------------------------------------------



app = Flask(__name__, static_url_path='/static')


@app.route('/')
def do_redirect():
    tmp = request
    return redirect('/static/index.html')


@app.route('/api/status')
def do_status():
    status = {}
    status['yellow'] =  True
    status['blue'] = False

    return jsonify(status)

@app.route('/api/led',methods=['post'])
def do_led():
    tmp = request;

    #if request.form['index'] == '1':
        #wiringpi.digitalWrite(LED_PIN_1,int(request.form['state']))

    #if request.form['index'] == '2':
    #    wiringpi.digitalWrite(LED_PIN_2,int(request.form['state']))


    return jsonify({'status':'ok'})



# 1
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # DO NOT IN PRODUCTION
