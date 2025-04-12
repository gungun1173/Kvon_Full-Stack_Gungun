# Fetch Random Jokes:
# Use https://api.chucknorris.io/jokes/random
# Fetch a random joke and print it.

import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
if response.status_code == 200:
   jokes = response.json()["value"]
   print("\n", jokes, "\n") 
else:
    print(f"Error : {response.status_code}")    
 