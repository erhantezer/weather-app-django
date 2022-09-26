from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint

# Create your views here.
def index(request):
    API_KEY=config("API_KEY")
    city = "Aksaray"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    content = response.json()
    pprint(content)
    pprint(content["name"])
    pprint(content["main"]["temp"])
    
    return render(request, "weather/index.html")




#! pprint sonucu aksaary için
# {'base': 'stations',
#  'clouds': {'all': 0},
#  'cod': 200,
#  'coord': {'lat': 38.3726, 'lon': 34.0254},
#  'dt': 1664202084,
#  'id': 324496,
#  'main': {'feels_like': 296.57,
#           'grnd_level': 908,
#           'humidity': 11,
#           'pressure': 1015,
#           'sea_level': 1015,
#           'temp': 297.77,
#           'temp_max': 297.77,
#           'temp_min': 297.77},
#  'name': 'Aksaray',
#  'sys': {'country': 'TR', 'sunrise': 1664163289, 'sunset': 1664206548},
#  'timezone': 10800,
#  'visibility': 10000,
#  'weather': [{'description': 'clear sky',
#               'icon': '01d',
#               'id': 800,
#               'main': 'Clear'}],
#  'wind': {'deg': 302, 'gust': 0.94, 'speed': 1.46}}