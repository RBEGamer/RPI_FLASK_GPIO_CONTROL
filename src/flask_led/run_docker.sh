#!/bin/bash
docker run -itd --name FLASK_LED_DEMO -p 5001:5000 --link couchdb:couchdb --privileged flask_led