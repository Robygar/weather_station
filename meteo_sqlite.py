import Adafruit_DHT
import sqlite3
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 3
COMPENSATION_TEMP = 0
COMPENSATION_HUMI= 0

con = sqlite3.connect("meteo.db")

while True:
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    hygr, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    hygr = hygr + COMPENSATION_HUMI  # compenso imprecisione sensore umidità
    temp = temp + COMPENSATION_TEMP  # compenso imprecisione sensore temperatura
    cursore = con.cursor()
    cursore.execute("INSERT INTO raspi_app_weather(temp, hygr, date) VALUES (?, ?, ?)", (temp, hygr, date))
    con.commit()
    print(cursore.rowcount)
    time.sleep(900)
