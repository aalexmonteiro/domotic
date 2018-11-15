import argparse, sys, os
sys.path.append(os.path.abspath(os.path.pardir))

import paho.mqtt.client as mqtt
from domotic.simulators.light import Light

def on_connect(client, userdata, flags, rc):
    client.subscribe('domatic/light')

def on_message(client, userdata, msg):
    print(msg.topic+' -  '+str(msg.payload))
    value = str(msg.payload)
    light = Light()
    light.save(value)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('127.0.0.1', 1883, 60)
client.loop_forever()