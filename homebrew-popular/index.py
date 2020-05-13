#!/usr/bin/env python3

## get most popular formula installs
import requests
import pprint
import os
import csv

## look for homebrew.csv in Documents folder for previous reviewed formulae
data_file = os.path.expanduser("~/Documents/homebrew.csv")

open(data_file,"a+").close()

with open(data_file, mode='r') as infile:
    reader = csv.reader(infile)
    reviewed = {rows[0]:rows[1] for rows in reader}

pp = pprint.PrettyPrinter(indent=4)

URL = "https://formulae.brew.sh/api/analytics/install/30d.json"

r = requests.get(url = URL)

data = r.json() 
limit = 5  
count_items = len(data["items"])
count_reviewed = len(reviewed)


top_items = [i for i in data["items"] if i['formula'] not in list(reviewed.keys())][:limit]
for formula in top_items:
    print(formula['formula'])


print("\n{} {} {}\n".format(limit,count_reviewed,count_items))