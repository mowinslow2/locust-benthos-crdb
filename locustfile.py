from math import cos, pi
import random
import time
import uuid
from locust import HttpUser, task

# Generate a random latitude and longitude values for the US (roughly according to ChatGPT)
def generate_random_lat_long():
    min_latitude, max_latitude = 24.396308, 49.384358
    min_longitude, max_longitude = -125.000000, -66.934570

    # Generate random latitude and longitude
    latitude = random.uniform(min_latitude, max_latitude)
    longitude = random.uniform(min_longitude, max_longitude)

    return latitude, longitude

def get_next_lat_long(self, latitude, longitude):
        # https://stackoverflow.com/questions/7477003/calculating-new-longitude-latitude-from-old-n-meters
        new_latitude  = latitude  + (1 / 6378) * (180 / pi)
        new_longitude = longitude + (1 / 6378) * (180 / pi) / cos(latitude * pi/180)

        return new_latitude, new_longitude

class TrackRides(HttpUser):
    @task
    def post_tracking_point(self):
        latitude, longitude = generate_random_lat_long()
        ride_id = uuid.uuid4()
        for point in range(100):
            self.client.post("/tracking", None, {"tracking":{"ride_id": str(ride_id), "latitude": latitude, "longitude":longitude}})
            latitude, longitude = get_next_lat_long(self, latitude, longitude) # generate new lat/long ~1 mile away 
            time.sleep(5)
            