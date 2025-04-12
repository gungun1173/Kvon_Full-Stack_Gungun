# Fetch Weather Data:
# Use https://api.open-meteo.com/v1/forecast
# Fetch current weather based on city and display.

import requests

city = input("Enter the city:")
url1 = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=411ee0a03513118dea40797c022da439"



response1 = requests.get(url1)
if response1.status_code == 200:
    lat = response1.json()
    latitude = lat[0]["lat"]
    print(latitude)
    longitude = lat[0]["lon"]
    print(longitude)
else:
    print(f"Error:{response1.status_code}")    

url2 = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=411ee0a03513118dea40797c022da439"
response = requests.get(url2)

if response.status_code == 200:
    dt = response.json()
    data = dt["weather"][0]["main"]
    print(data)
  
else:
    print(f"Error:{response1.status_code}")    



  
