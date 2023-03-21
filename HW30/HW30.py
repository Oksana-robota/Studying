import requests
import random
import re

# 1
list_sources = ['https://www.google.com/', 'https://www.facebook.com/',
                'https://twitter.com/', 'https://www.amazon.com/', 'https://www.apple.com/']
s = random.choice(list_sources)
get_req = requests.get(s)
title = re.search(r'(?<=ww\.|:\/\/)[\w]+(?=\.com\/)', s)
print(f'Status code: {get_req.status_code}')
print(f'Title: {str(title.group(0)).title()}')
print(f'HTML code length: {len(get_req.text)}')

# 2
town = input()
coord = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={town}')
latitude, longitude, timezone = '','',''
for i in coord.json()['results']:
    if i['name'] == town:
        latitude = i['latitude']
        longitude = i['longitude']
        timezone = i['timezone']
        break
weather = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}'
                       f'&longitude={longitude}&timezone={timezone}&current_weather=true')
print(f'Current weather in {town}')
for k, v in weather.json()['current_weather'].items():
    print(f'{k.title()}: {v}')
