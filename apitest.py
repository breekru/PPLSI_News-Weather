import requests
from pyld import jsonld
import json
#response_API = requests.get('https://api.weather.gov/gridpoints/OUN/127,61/forecast')
response_API = jsonld.expand('https://api.weather.gov/gridpoints/OUN/127,61/forecast')
print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data) 
#active_case = parse_json['periods'][1]['temperature']
print("Temperature:", parse_json)
