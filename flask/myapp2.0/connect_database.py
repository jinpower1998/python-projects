
import json
from app import *
import requests as rq

url = ""

class connect_database():

    def get_data():
        requested_data = rq.get(url)
        return requested_data

    def post_data():
        return 0



