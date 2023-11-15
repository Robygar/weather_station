# weather_station
Create a weather station with raspberry_pi, python and django framework, with graphical output and json.
This project, takes temperature and humidity from a DHT11 sensor with a python program (it is possible to use DHT22 for more accurate results)and saves the data at 15-minute intervals to a Sqlite database, with the django framework this data is taken from the database and printed in jason format (without serializer) and in chart.js.
 
# instructions:
- download the project to the raspberry (e.g., /home/pi/weather/)
- install adafriut from official repository:``` https://pypi.org/project/Adafruit-DHT/```
- connect the sensor (in the project it is connected to pin 3)
- install the django framework
  ```
  python pip install Django
  ```
- place in the folder where the manage.py file is and give the commands:
```
python manage.py makemigrations raspi_app
python manage.py migrate
python manage.py runserver
```
at this point you can see the server running by going to the 
```
http://127.0.0.1:8000/get_weather_data/ 
```
page to get the data in json format or 
```
http://127.0.0.1:8000/weather_chart/ 
```
for the graph.
Now it will be empty with no data, to start loading data you need to run meteo_sqlite.py so run: 
```
python meteo_sqlite.py
```
or if you want it to run in the background 
```
nohup python meteo_sqlite.py &
```
You can also use ginx and gunicorn to deploy
