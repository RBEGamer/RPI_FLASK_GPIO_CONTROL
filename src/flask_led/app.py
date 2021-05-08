# 1
from flask import Flask, redirect, request, jsonify
import json  # FOR THE REST API
import os
from paho.mqtt import client as mqtt_client
#---- SETUP THE DATABASE -----#
#CLEAR THE DATABASE
#couch_client = CouchDB('admin', 'admin', url='http://' + DB_IP + ':5984', connect=True)
#log_db = couch_client['logs']
#for document in log_db:
#    document.delete()
#couch_client.disconnect();


#
#---------------------------------------------------------------------

broker = '127.0.0.1'
port = 1883
topic = "/data/temp"

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"{random.randint(0, 100)}"
        result = client.publish(topic, msg)


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
    global client
    tmp = request;
    client.publish(topic, request.form['index'])
    return jsonify({'status':'ok'})



# 1
if __name__ == '__main__':
    client = connect_mqtt()
    client.loop_start()
    app.run(debug=True, host='0.0.0.0', port=5000)  # DO NOT IN PRODUCTION
