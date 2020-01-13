# 1
from flask import Flask, redirect, request, jsonify
import json  # FOR THE REST API
import os
import wiringpi
from cloudant.client import Cloudant as CouchDB
DB_IP = "127.0.0.1"
if 'COUCHDB_PORT_5984_TCP_ADDR' in os.environ:
    print("IM RUNNING IN DOCKER")
    DB_IP = os.environ['COUCHDB_PORT_5984_TCP_ADDR']



# 11
wiringpi.wiringPiSetup()
# SETUP PINS
LED_PIN_1 = 7
LED_PIN_2 = 0
BUTTON_YELLOW_PIN = 9
BUTTON_BLUE_PIN = 8
# SET TO OUTPUT
wiringpi.pinMode(LED_PIN_1, 1)
wiringpi.pinMode(LED_PIN_2, 1)
wiringpi.digitalWrite(LED_PIN_1, 0)
wiringpi.digitalWrite(LED_PIN_2, 0)

# 12
# SET INPUT
wiringpi.pinMode(BUTTON_YELLOW_PIN, 0)
wiringpi.pinMode(BUTTON_BLUE_PIN, 0)
# ENABLE PULLUP
wiringpi.pullUpDnControl(BUTTON_YELLOW_PIN, 2)
wiringpi.pullUpDnControl(BUTTON_BLUE_PIN, 2)

# 1
app = Flask(__name__, static_url_path='/static')


# 2
@app.route('/')
def index_redirect():
    return redirect("/static/index.html", code=302)


# 3
@app.route('/api/status', methods=['get'])
def api_status():
    global wiringpi
    status = {}
    status['button_yellow'] = not bool(wiringpi.digitalRead(BUTTON_YELLOW_PIN))
    status['button_blue'] = not bool(wiringpi.digitalRead(BUTTON_BLUE_PIN))
    return jsonify(status)


# 8
@app.route('/api/set_led', methods=['post'])
def set_led():
    global wiringpi
    global DB_IP
    # 9
    content = request.form
    print(content['led_index'])

    # 10
    if int(content['led_index']) == 1:
        wiringpi.digitalWrite(LED_PIN_1, int(content['status']))  # 12
    elif int(content['led_index']) == 2:
        wiringpi.digitalWrite(LED_PIN_2, int(content['status']))  # 12

    # 13 -- DATABSE WRITE DOCUEMTENT --
    couch_client = CouchDB('admin', 'admin', url='http://' + DB_IP + ':5984', connect=True)
    log_db = couch_client['logs']
    doc = log_db.create_document(
        {'action': "SET LED " + str(content['led_index']) + " BY USER TO " + str(content['status'])})
    couch_client.disconnect();

    return jsonify({'status': 'ok'})


# 14
@app.route('/api/get_log', methods=['get'])
def get_log():
    global DB_IP
    logs = [];
    couch_client = CouchDB('admin', 'admin', url='http://' + DB_IP + ':5984', connect=True)
    log_db = couch_client['logs']
    for document in log_db:
        logs.append(document)
    couch_client.disconnect();
    return jsonify(logs)


# 1
@app.route('/favicon.ico')
def get_favicon_ico():
    return app.send_static_file('/static/favicon.ico')


# 1
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # DO NOT IN PRODUCTION
