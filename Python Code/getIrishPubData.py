import json
import csv
import numpy as np
import pandas as pd
import time
import googlemaps as gm

gmaps = gm.Client(key=)

cities = []
irishPubs = {}
count = 0

""" Create variable cities with all city names """
try:
    with open('cities.json') as json_file:
        cities = json.load(json_file)
    json_file.close()
    print(len(cities))
except FileNotFoundError:
    with open('worldcities.csv', newline='') as csvfile:
        cityreader = csv.reader(csvfile, delimiter=',')
        for row in cityreader:
            cities.append({
                "city": row[0],
                "done": False
            })
        cities.pop(0)
    csvfile.close()
    with open('cities.json', 'w') as outfile:
        outfile.write(json.dumps(cities, indent=4))
    outfile.close()

""" See if irish pubs file already exists, if so continue with that one """
try:
    with open('pubs.json') as pubs_file:
        irishPubs = json.load(pubs_file)
    pubs_file.close()
    print(len(irishPubs))
except FileNotFoundError:
    None

def getIrishPubs(location, next_page_token=None):
    if next_page_token:
        newIrishPubs = gmaps.places('irish pub ' + location, page_token=next_page_token)
    else:
        newIrishPubs = gmaps.places('irish pub ' + location)
    time.sleep(2)
    if newIrishPubs['status'] == 'OK':
        for pub in newIrishPubs['results']:
            irishPubs[pub['place_id']] = {
                "place": pub,
                "details": False
            }
        
        if 'next_page_token' in newIrishPubs.keys():
            getIrishPubs(location, newIrishPubs['next_page_token'])

for city in cities:
    if city['done'] == False:
        count += 1
        getIrishPubs(city['city'])
        city['done'] = True
        if count % 100 == 0:
            print(len(irishPubs))
        if count % 5000 == 0:
            break

with open('cities.json', 'w') as outfile:
        outfile.write(json.dumps(cities, sort_keys=True, indent=4))

with open('pubs.json', 'w') as outfile:
    outfile.write(json.dumps(irishPubs, sort_keys=True, indent=4))
