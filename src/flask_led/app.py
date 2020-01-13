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
#CLEAR THE DATABASE
couch_client = CouchDB('admin', 'admin', url='http://' + DB_IP + ':5984', connect=True)
log_db = couch_client['logs']
for document in log_db:
    document.delete()
couch_client.disconnect();


#---------------------------------------------------------------------

app = Flask(__name__, static_url_path='/static')









# 1
@app.route('/favicon.ico')
def get_favicon_ico():
    return app.send_static_file('/static/favicon.ico')

# 1
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # DO NOT IN PRODUCTION
