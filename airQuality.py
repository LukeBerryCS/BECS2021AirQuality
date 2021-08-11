#BECS Project #2: Air Quality
#By Luke Berry

from geopy.geocoders import Nominatim
import requests

token = "ff3ea885409f0bfe3dd123ee299819312329effc"

print("Welcome to PyAirQuality.")
#Getting user input for zip code, and changing from string to integer
zipcode = input("What zip code would you like air quality data for? ")
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

pm25ForecastDay = info['data']['forecast']['daily']['pm25'][3]['day']
pm25ForecastAvg = info['data']['forecast']['daily']['pm25'][3]['avg']
pm25ForecastMax = info['data']['forecast']['daily']['pm25'][3]['max']
pm25ForecastMin = info['data']['forecast']['daily']['pm25'][3]['min']

print(f'Station location: {city}\n')
print(f'Current Air Quality Index: {aqi}')
print(f'Current PM2.5 value: {pm25}\n')

print(f'Forecast: {pm25ForecastDay}\n')
print(f'Average PM2.5: {pm25ForecastAvg}')
print(f'Minimum PM2.5: {pm25ForecastMin}')
print(f'Maximum PM2.5: {pm25ForecastMax}')



 