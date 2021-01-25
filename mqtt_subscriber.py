import sqlite3
import paho.mqtt.client as client
con=sqlite3.connect("topicdb.db")
def on_connect(client,userdata,flag,rc):
    print("Connect with {rc}")
    client.subscribe("rsp/pub")
    cursor=con.cursor
    cursor.execute('CREATE TABLE IF NOT EXISTS mqttMessagetb(id INTEGER PRIMARY KEY AUTOINCREMENT,mtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,msg VARCHAR(100))')
def on_message(client,userdata,msg):
    print(f"Message from is - {msg.topic} and msg - {msg.payload}")
    cursor=con.cursor
    cursor.execute("INSERT INTO mqttMessagetb(msg)VALUES('''+str(msg.payload.decode('UTF-8'))+''')")
    con.commit()
client=mqtt.Client()
client.on_connect=on_connect
client.on_message=on_message
client.connect("broker.emqx.io",1883,60)
client.loop_forever()