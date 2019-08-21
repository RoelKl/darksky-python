import requests
import json
import datetime

request_url = 'https://api.darksky.net/forecast/a4848c6efc250bc969f3cd235a53e9f3/52.449263,5.834519?units=si'
result = requests.get(request_url).json()
print(datetime.datetime.fromtimestamp(result['currently']['time']), result['currently']['temperature'],result['currently']['pressure'])
for r in result['hourly']['data']:
    print(datetime.datetime.fromtimestamp(r['time']), r['temperature'],r['pressure'])

