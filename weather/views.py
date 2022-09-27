from django.contrib import messages
from django.shortcuts import render,get_object_or_404, redirect
from decouple import config
import requests
from pprint import pprint

from weather.models import City

# Create your views here.
def index(request):
    API_KEY=config("API_KEY") #! api keyi env içinden config ile alıyoruz
    city = "Aksaray"
    u_city = request.POST.get("name") #! formda gönderdiğimiz "name" yakalıyoruz
    
    if u_city:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={u_city}&appid={API_KEY}&units=metric"
        response =requests.get(url) #!url istek atıp cevap döndürdük
        
        if response.ok:
            content = response.json() #! cevap varsa url den gelen verileri json yapısına çevir contente aktar
            r_city = content["name"] #! content içinden  şehir adını al ve r_city aktar
            
            if City.objects.filter(name = r_city): #! şehir ismi database de varsa (City model sinde) 
                messages.warning(request, "City already exists!")
            else:
                City.objects.create(name=r_city) #! yoksa City modelsi yardımıyla database kaydeder
    
    
    #! database kaydedilen veri çekilip ihtiyaç olan kısımlar liste içine atılıp template içinde for döngüsüyle kullanacağız
    city_data =[]
    cities =City.objects.all()
    for city in cities:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        content = response.json()
        data = {
            "city":city,
            "temp" : content["main"]["temp"],
            "icon" : content["weather"][0]["icon"],
            "desc" : content["weather"][0]["description"]
        }
        city_data.append(data)
        
        context = {
            "city_data":city_data
        }
    
    
    return render(request, "weather/index.html", context)


def delete_city(request, id):
    #* city = City.objects.get(id=id)
    city = get_object_or_404(City, id=id)
    city.delete()
    messages.warning(request, "City deleted.")
    return redirect("home")

# pprint(content)
    # pprint(content["name"])
    # pprint(content["main"]["temp"])


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