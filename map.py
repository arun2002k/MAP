import phonenumbers
import opencage
import folium
from ph_no import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

# your API key from Opencagedata.com
key = ''

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

mymap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(mymap)

mymap.save("location.html")