import Adafruit_DHT
import sqlite3
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 3  #dht sensor pin
COMPENSATION_TEMP = 0  #modify to calibrate temperature
COMPENSATION_HUMI= 0 #modify to calibrate humidity

con = sqlite3.connect("meteo.db")

while True:
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    hygr, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    hygr = hygr + COMPENSATION_HUMI 
    temp = temp + COMPENSATION_TEMP 
    cursore = con.cursor()
    cursore.execute("INSERT INTO raspi_app_weather(temp, hygr, date) VALUES (?, ?, ?)", (temp, hygr, date))
    con.commit()
    print(cursore.rowcount)
    time.sleep(900) # 900 seconds 
