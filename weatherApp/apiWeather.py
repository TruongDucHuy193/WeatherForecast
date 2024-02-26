from geopy.geocoders import Nominatim

#nhận api
def get_api(self):
    with open("weatherApp/apiKey.txt",'r') as api_file:
        api_key = api_file.read().strip()
    return api_key

#lấy dữ liệu thời tiết
def getWeather(self):
    city = self.textfield.get()
    geolocator = Nominatim(user_agent="geoapiExcercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    self.timezone.config(text=result)
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    self.clock.config(text=current_time)

    #đường dẫn lấy dữ liệu thời tiết
    api_key = self.get_api()
    api = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly,daily&appid="+api_key
    json_data = requests.get(api).json()

    #current
    temp = json_data["current"]["temp"]
    humidity = json_data["current"]["humidity"]
    pressure = json_data["current"]["pressure"]
    wind = json_data["current"]["wind_speed"]
    visibility = json_data["current"]["visibility"]
    #descripption = json_data["current"]["weather"][0]["description"]
    
    self.t.config(text=f"{temp} °C")
    self.h.config(text=f"{humidity} %")
    self.p.config(text=f"{pressure} mb")
    self.w.config(text=f"{wind} km/h")
    self.v.config(text=f"{visibility} km")
    