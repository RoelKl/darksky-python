import requests
import pandas as pd

request_url = 'https://api.darksky.net/forecast/a4848c6efc250bc969f3cd235a53e9f3/52.449263,5.834519?units=si'
result = requests.get(request_url).json()
print(result)
df = pd.DataFrame.from_dict(json_normalize(result), orient='columns')
print(df.head())
