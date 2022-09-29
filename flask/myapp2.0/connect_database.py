
import json, boto3
from boto3.dynamodb.conditions import Key, Attr
from app import *


dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table('simple-web-app')

class connect_database():

    def get_data(email):
        requested_data = table.query(
        KeyConditionExpression=Key('Email').eq(email) 
        )
        
        items = requested_data["Items"]
        return items

    def post_data():
        return 0

response = connect_database.get_data("test@test.de")

for i in response:
    print(i["Password"], i["Firstname"])