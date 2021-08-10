#BECS Project #2: Air Quality
#By Luke Berry

from geopy.geocoders import Nominatim
import requests

token = "ff3ea885409f0bfe3dd123ee299819312329effc"

print("Welcome to PyAirQuality.")
#Getting user input for zip code, and changing from string to integer
zipcode = input("What zip code would you like air quality data for?")
zipcode = int(zipcode)
print("Searching for data...this may take awhile")
#Getting a geological location based on the user inputted zip code
geolocator = Nominatim(user_agent = "airQuality.py")
location = geolocator.geocode({"postalcode":zipcode})
#Assigning the long/lat properties of the location object to variables for use in url




latitude = location.latitude
longitude = location.longitude

url = f"https://api.waqi.info/feed/geo:{latitude};{longitude}/?token={token}"
info = requests.get(url).json()

aqi = info['data']['aqi']
pm25 = info['data']['iaqi']['pm25']['v']
city = info['data']['city']['name']

print(f'Current Air Quality Index: {aqi}')
print(f'Current PM2.5 value: {pm25}')
print(f'Station location: {city}')

 