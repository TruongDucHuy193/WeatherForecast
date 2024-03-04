from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
from threading import *
import requests
import pytz

#nhận api
def get_api():
    with open("weatherApp/apiKey.txt",'r') as api_file:
        api_key = api_file.read().strip()
    return api_key

def get_weather(key, city):
    geolocator = Nominatim(user_agent="geoapiExcercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    timezone_result = obj.timezone_at(lng=location.longitude, lat=location.latitude)  # Đổi tên biến này thành timezone_result
    home = pytz.timezone(timezone_result)  # Sử dụng tên biến mới này khi cần thiết
    local_time = datetime.now(home)
    week_day = local_time.strftime("%w")
    day = local_time.strftime("%d")
    times = local_time.strftime("%H:%M")

    #đường dẫn lấy dữ liệu thời tiết
    api = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&units=metric&lang=en&appid={key}"
    json_data = requests.get(api).json()

    #current
    temp = json_data["main"]["temp"]
    temp_max = json_data["main"]["temp_max"]
    temp_min = json_data["main"]["temp_min"]
    humidity = json_data["main"]["humidity"]
    pressure = json_data["main"]["pressure"]
    wind = json_data["wind"]["speed"]
    visibility = json_data["visibility"]
    description = json_data["weather"][0]["description"]
    
    json = [(temp, temp_max, temp_min, humidity, pressure, wind, visibility/1000, description, timezone_result),
            (week_day, day, times)],
    return json

def get_weather_4days_hourly(key, city):
    geolocator = Nominatim(user_agent="geoapiExcercises")
    location = geolocator.geocode(city)
    
    #đường dẫn lấy dữ liệu thời tiết
    api = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={location.latitude}&lon={location.longitude}&units=metric&lang=en&appid={key}"
    json_data = requests.get(api).json()

def get_weather_7days(key, city):
    geolocator = Nominatim(user_agent="geoapiExcercises")
    location = geolocator.geocode(city)

    #đường dẫn lấy dữ liệu thời tiết
    api = f"api.openweathermap.org/data/2.5/forecast/daily?lat={location.latitude}&lon={location.longitude}&cnt=7&units=metric&lang=en&appid={key}"
    json_data = requests.get(api).json()["list"]
    day_current = json_data[0]
    day1 = json_data[1]
    day2 = json_data[2]
    day3 = json_data[3]
    day4 = json_data[4]
    day5 = json_data[5]
    day6 = json_data[6]
