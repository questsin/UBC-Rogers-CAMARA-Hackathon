import requests
import json
from math import sqrt
import numpy as np

URL = "https://pplx.azurewebsites.net/api/rapid/v0/location-verification/verify"
ACCESS_TOKEN = # YOUR ACCESS TOKEN
PHONE_NUMBER = # YOUR PHONE NUMBER
HEADERS = {"Authorization": "Bearer " + ACCESS_TOKEN,
           "Cache-Control": "no-cache",
           "accept": "application/json",
           "Content-Type": "application/json"}


ACCURACY = 0.001

# Any three points on the map with reasonable distance in-between would work
# as long as the points are not aligned on a line.
# These three are random points around Canada. First is on the pacific ocean,
# second one is on the Hudson Bay, third one is on the Atlantic ocean.
markers = [[50, -130], [60, -90], [40, -60]]


def find_distance_from_marker(marker):
    print("SEARCH DISTANCE FOR MARKER", marker)
    a, b = 0, 180
    while abs(a - b) > ACCURACY:
        if user_inside_perimeter(marker[0], marker[1], ((a+b) / 2)):
            b = ((a + b) / 2)
        else:
            a = ((a + b) / 2)
    return (a + b) / 2


def user_inside_perimeter(latitude, longitude, accuracy):
    data = json.dumps({"device": {"phoneNumber": PHONE_NUMBER},
                       "area": {
                           "type": "Circle",
                           "location": {
                               "latitude": latitude,
                               "longitude": longitude
                           },
                           "accuracy": accuracy
                       }})

    res = requests.post(URL, data=data, headers=HEADERS)
    print(res.json()["area"]["accuracy"], res.json()["verificationResult"],)
    return res.json()["verificationResult"]


# Math from https://stackoverflow.com/questions/9747227/2d-trilateration
def trilateriation(markers, distances):
    p1 = np.array(markers[0])
    p2 = np.array(markers[1])
    p3 = np.array(markers[2])
    r1 = distances[0]
    r2 = distances[1]
    r3 = distances[2]
    d = np.linalg.norm(p2 - p1)
    ex = (p2 - p1) / d
    i = np.dot(ex, (p3 - p1))
    ey = (p3 - p1 - i * ex) / np.linalg.norm(p3 - p1 - i * ex)
    j = np.dot(ey, (p3 - p1))
    x = (r1*r1 - r2*r2 + d*d) / (2 * d)
    y = ((r1*r1 - r3*r3 + i*i + j*j) / (2 * j)) - (i * x / j)
    return p1 + x*ex + y*ey


if len(markers) != 3:
    print("Exactly three markers are required")
    exit(1)

distances = []
for m in markers:
    distances.append(find_distance_from_marker(m))
print(trilateriation(markers, distances))
