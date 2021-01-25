import sqlite3
import time
import board
import adafruit_dht
dhtDevice=adafruit_dh.DHT11(board.D4)
con=sqlite3.connect("humiditydb.db")
sql_cmd="CREATE TABLE IF NOT EXISTS humiditytb(c_value FLOAT,f_value FLOAT,humidity FLOAT)"
cursor=con.cursor()
cursor.execute(sql_cmd)
while True:
    try:
        temp_c=dhtDevice.temparaure
        temp_f=temp_c*(9/5)+32
        humidity=dhtDevice.humidity
        print("Temp: {:.1f} F / {:.1f} C Humidity: {}%".format(temp_f,temp_c,humidity))
        sql_cmd="INSERT INTO humiditytb VALUES(?,?,?);"
        print(sql_cmd)
        cursor.execute(sql_cmd,{temp_c,temp_f,humidity})
        con.commit()
        cursor.execute("SELECT * FROM humiditytb")
        rows=cursor.fetchall()
        for r in rows:
            print(r)
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(5)
con.close()