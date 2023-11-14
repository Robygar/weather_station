from django.shortcuts import render
from django.http import JsonResponse
from .models import Weather

def weather_chart(request):
    data = Weather.objects.all()
    labels = [str(entry.date) for entry in data]
    temperatures = [entry.temp for entry in data]
    humidity = [entry.hygr for entry in data]

    chart_data = {
        'labels': labels,
        'temperatures': temperatures,
        'humidity': humidity,
    }

    return render(request, 'raspi_app/weather_chart.html', {'chart_data': chart_data})

def get_weather_data(request):
    data = Weather.objects.all()
    labels = [str(entry.date) for entry in data]
    temperatures = [entry.temp for entry in data]
    humidity = [entry.hygr for entry in data]

    return JsonResponse({'labels': labels, 'temperatures': temperatures, 'humidity': humidity})
