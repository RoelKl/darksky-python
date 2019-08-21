import requests
import json
import datetime
import sqlite3
import os

request_url = 'https://api.darksky.net/forecast/a4848c6efc250bc969f3cd235a53e9f3/52.449263,5.834519?units=si'
dbase = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'darksky.sqlite'

try:
    result = requests.get(request_url).json()
    # datetime.datetime.fromtimestamp(result['currently']['time'])
    now_dttim = result['currently']['time']
    now_temp = result['currently']['temperature']
    now_pressure = result['currently']['pressure']
except:
    print('data could not be fetched\nprogram will exit')
    exit()
conn = sqlite3.connect(dbase)
cur = conn.cursor()
cur.execute('insert into Now (dttim, temp, pressure) values(?, ?, ?)',
            (now_dttim, now_temp, now_pressure))
cur.execute('select id from Now where dttim = ?', (now_dttim,))
now_id = cur.fetchone()[0]
for r in result['hourly']['data']:
    cur.execute('insert into Expectation (nowId, dttim, temp, pressure) values(?, ?, ?, ?)',
                (now_id, r['time'], r['temperature'], r['pressure']))
conn.commit()
conn.close()
