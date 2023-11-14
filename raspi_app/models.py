# raspi_app/models.py

from django.db import models

class Weather(models.Model):
    temp = models.FloatField()
    hygr = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return f'Temperature: {self.temp}, Humidity: {self.hygr}, Date: {self.date}'

class WeatherData(models.Model):
    temp = models.FloatField()
    hygr = models.FloatField()
    date = models.DateTimeField()

    def __str__(self):
        return f'Temperature: {self.temp}, Humidity: {self.hygr}, Date: {self.date}'
