from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
#nhận api
def get_api():
    with open("weatherApp/apiKey.txt",'r') as api_file:
        api_key = api_file.read().strip()
    return api_key

#lấy dữ liệu thời tiết
def getWeather(KEY, city):
    geolocator = Nominatim(user_agent="geoapiExcercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    timezone_result = obj.timezone_at(lng=location.longitude, lat=location.latitude)  # Đổi tên biến này thành timezone_result
    home = pytz.timezone(timezone_result)  # Sử dụng tên biến mới này khi cần thiết
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")

    #đường dẫn lấy dữ liệu thời tiết
    api = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly,daily&appid="+KEY
    json_data = requests.get(api).json()

    #current
    temp = json_data["current"]["temp"]
    humidity = json_data["current"]["humidity"]
    pressure = json_data["current"]["pressure"]
    wind = json_data["current"]["wind_speed"]
    visibility = json_data["current"]["visibility"]
    #descripption = json_data["current"]["weather"][0]["description"]
    
    return [temp,humidity,pressure,wind,visibility, timezone_result]
    