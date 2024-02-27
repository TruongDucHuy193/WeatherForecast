import geocoder
from timezonefinder import TimezoneFinder

def get_current_local():
    g = geocoder.ip('me')
    lat, lng = g.latlng
    obj = TimezoneFinder()
    city = obj.timezone_at(lng=lng, lat=lat).split("/")[1].replace("_", " ")
    return city