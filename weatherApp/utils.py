import geocoder
from timezonefinder import TimezoneFinder

def get_current_local():
    g = geocoder.ip('me')
    lat, lng = g.latlng
    location = geocoder.osm([lat, lng], method='reverse')
    district = location.raw['address']['suburb'].split(" ", 1)[1].strip()
    return district