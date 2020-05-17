#!/usr/bin/env python3

## problem: we want to rename the key 'formula' to 'xyzzy'

import requests

## for loop
def method1(data):
    for item in data['items']: item['xyzzy'] = item.pop('formula')
    print(data['items'][0])

## more pythonic way with nested comprehension
def rename(k):
    return k if k != 'formula' else 'xyzzy'

def method2(data):
    data['items'] = [ {rename(k):v for k,v in item.items()} for item in data['items']]
    print(data['items'][0])

URL = "https://formulae.brew.sh/api/analytics/install-on-request/30d.json"
r = requests.get(url = URL)
data = r.json() 
print(data['items'][0])
method1(r.json())
method2(r.json())