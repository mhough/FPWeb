#!/usr/bin/env python
import json
import requests
from demodata import demodata


for record in demodata['data']:
  r = requests.post('http://localhost:5000/datapost', data=json.dumps(record))
  assert r.status_code == 200, r.status_code
  assert r.headers['content-type'] == 'text/html', r.headers['content-type']
  print r.text


print '-' * 70
print 'Okay!'
