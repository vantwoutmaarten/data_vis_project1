import json
import csv
import numpy as np
import pandas as pd
import time

irishPubs = {}

irishPubsClipped = {}

""" See if irish pubs file already exists, if so continue with that one """
try:
    with open('pubs.json') as pubs_file:
        irishPubs = json.load(pubs_file)
    pubs_file.close()
    print(len(irishPubs))
except FileNotFoundError:
    None

for pub in irishPubs:
    name = irishPubs[pub]['place']['name']
    coord = irishPubs[pub]['place']['geometry']['location']
    irishPubsClipped[pub] = {
        'name' : name,
        'lat' : coord['lat'],
        'lng' : coord['lng']
    }

with open('pubsClipped.json', 'w') as outfile:
    outfile.write(json.dumps(irishPubsClipped, sort_keys=True, indent=4))

### EXAMPLE IRISH PUB ###
# "ChIJ---ZjYnEwogRac3_vO7j4LM": {
#     "details": false,
#     "place": {
#         "formatted_address": "813 N Tampa St, Tampa, FL 33602, United States",
#         "geometry": {
#             "location": {
#                 "lat": 27.9510154,
#                 "lng": -82.46014520000001
#             },
#             "viewport": {
#                 "northeast": {
#                     "lat": 27.95232802989272,
#                     "lng": -82.45889702010729
#                 },
#                 "southwest": {
#                     "lat": 27.94962837010727,
#                     "lng": -82.46159667989274
#                 }
#             }
#         },
#         "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/bar-71.png",
#         "id": "dfd59e612d7480e6a60054158282d73fdd4120a4",
#         "name": "The Local Draught House",
#         "opening_hours": {
#             "open_now": false
#         },
#         "photos": [
#             {
#                 "height": 3264,
#                 "html_attributions": [
#                     "<a href=\"https://maps.google.com/maps/contrib/116763113628140827666\">Paddywagon Irish Pub</a>"
#                 ],
#                 "photo_reference": "CmRaAAAAbJ3JUnyuV2aXK7H5UiVZcJQSCEqswcfovXt-NaGXMenCTuHP8Pn8I7sRt6633evDyddyaMFZC_gOJ17DTO0sNc9XjXtFzjzQ3pGDq8ml3nIU3NsmUAHDfLk-qepO0w5EEhDBif2K6efMjOYdKZzXYoi2GhQMjfML898NfC5yNtVnqPMH7mm3Uw",
#                 "width": 4360
#             }
#         ],
#         "place_id": "ChIJ---ZjYnEwogRac3_vO7j4LM",
#         "plus_code": {
#             "compound_code": "XG2Q+CW Tampa, Florida, United States",
#             "global_code": "76VVXG2Q+CW"
#         },
#         "rating": 4.4,
#         "reference": "ChIJ---ZjYnEwogRac3_vO7j4LM",
#         "types": [
#             "bar",
#             "restaurant",
#             "food",
#             "point_of_interest",
#             "establishment"
#         ],
#         "user_ratings_total": 331
#     }
# },