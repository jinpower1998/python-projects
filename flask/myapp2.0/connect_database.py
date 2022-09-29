
import json
from app import *
import requests as rq

url = "http://localhost:5000/"

class connect_database():

    def get_data():
        requested_data = json.dumps(rq.get(url))
        return requested_data

    def post_data():
        pass



