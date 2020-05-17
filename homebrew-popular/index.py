#!/usr/bin/env python3

## get most popular formula installs
import requests
import pprint
import os
import csv

def addkey(data, key,value):
    for item in data['items']:
        item[key] = value;
    return data

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def string_to_float(v):
    return float(v) if isfloat(v) else v

def rename(k):
    return k if k not in ['formula','cask'] else 'name'

def standardize(items):
    ## todo 05/17/2020 combine/improve/pythonic this

    ## rename formula/cask to name
    items = [ {rename(k):string_to_float(v) for k,v in item.items()} for item in items]

    ## remove any items that start with 'lnkd'
    new_items = []
    for item in items:
        if 'lnkd' not in item['name']:
            new_items.append(item)

    ## sort by percent desc
    new_items = sorted(new_items, key = lambda i: i['percent'],reverse=True) 

    items = new_items

    return items

## look for homebrew.csv in Documents folder for previous reviewed formulae
data_file = os.path.expanduser("~/Documents/homebrew.csv")

open(data_file,"a+").close()

with open(data_file, mode='r') as infile:
    reader = csv.reader(infile)
    reviewed = {rows[0]:rows[1] for rows in reader}

pp = pprint.PrettyPrinter(indent=4)

URL = "https://formulae.brew.sh/api/analytics/install-on-request/30d.json"
r = requests.get(url = URL)
formulas = addkey(r.json(),'source','formula')

URL = "https://formulae.brew.sh/api/analytics/cask-install/30d.json"
r = requests.get(url = URL)
casks = addkey(r.json(),'source','cask')

data = formulas['items'] + casks['items']

data = standardize(data)

limit = 5
count_items = len(data)
count_reviewed = len(reviewed)

top_items = [i for i in data if i['name'] not in list(reviewed.keys())][:limit]
for item in top_items:
    print(item['name'],item['source'],item['percent'])


print("\n{} {} {}\n".format(limit,count_reviewed,count_items))