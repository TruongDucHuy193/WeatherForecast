import geocoder
from timezonefinder import TimezoneFinder

def get_current_local():
    g = geocoder.ip('me')
    lat, lng = g.latlng
    location = geocoder.osm([lat, lng], method='reverse')
    district = location.raw['address']['suburb'].replace("Quận", "").replace("Huyện", "").replace("Thành phố", "").replace("Phường", "").replace("Xã", "").replace("Thị trấn", "").strip()
    return district
