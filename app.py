import socket
import time
import paho.mqtt.client as mqtt
from flask import Flask, render_template, json, request
from domotic.simulators.air_conditioner import AirConditioner
from domotic.simulators.light import Light
from domotic.simulators.tv import TV
from domotic.simulators.audio_system import AudioSystem

app = Flask(__name__)

def request_socket(host, port, value):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(value.encode('utf-8'))
        s.close()
    except Exception as e:
        return json.dumps({'error':str(e)})

def request_mqtt(url, value):
    mqttc = mqtt.Client()
    mqttc.connect('127.0.0.1', 1883)
    mqttc.publish('domatic/' + url, value)

def process(req, url, device, host=None, port=None):
    value = req.form['value']
    req_type = req.form['reqType']
    if req_type == 'mqtt':
        request_mqtt(url, value)
    else:
        request_socket(host, port, value)
    
    return device.get().decode('utf-8')


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/changeAir',methods=['POST','GET'])
def changeAir():
    air = AirConditioner()
    res = process(request, 'air', air, '127.0.0.2', 65432)
    return res

@app.route('/changeLight',methods=['POST','GET'])
def changeLight():
    light = Light()
    res = process(request, 'light', light, '127.0.0.3', 65433)
    return res

@app.route('/changeTV',methods=['POST','GET'])
def changeTV():
    tv = TV()
    res = process(request, 'tv', tv, '127.0.0.4', 65434)
    return res

@app.route('/changeAudio',methods=['POST','GET'])
def changeAudio():
    audio = AudioSystem()
    res = process(request, 'audio', audio, '127.0.0.5', 65435)
    return res


if __name__ == "__main__":
    app.run(port=5002)
