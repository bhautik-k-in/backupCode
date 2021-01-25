import paho.mqtt.client as mqtt
import time
def on_connect(client,userdata,flag,rc):
    print("Connect with {rc}")
client=mqtt.Client()
client.on_connect=on_connect
client.connect("broker.emqx.io",1883,60)
while True:
    inp=input("Enter your msg - ")
    client.publish("rsp.pub",payload=inp,qos=0,retain=False)
    print("Send to rsp/pub")
client.loop_forever()