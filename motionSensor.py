import time
import sqlite3
import RPi.GPIO as GPIO
con=sqlite3.connect("motiondb.db")
cursor=con.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS motiontb(current_date DATE,current_time TIME,msg TEXT)')
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)
while True:
    input_state=GPIO.input(18)
    if input_state==True:
        print('Motion Detected')
        cursor.execute('''INSERT INTO motiontb(current_date,current_time,msg)VALUES(CURRENT_DATE,CURRENT_TIME,'Motion Detected')''')
        time.sleep(5)
con.commit()
con.close()