
import boto3
from boto3.dynamodb.conditions import Key
from app import *

# define resource dynamodb
dynamodb = boto3.resource("dynamodb")
# choose table 
table = dynamodb.Table('simple-web-app')



class connect_database():

    # query data by key "Email"
    def get_data(email):
        requested_data = table.query(
        KeyConditionExpression=Key('Email').eq(email) 
        )
        
        items = requested_data["Items"]
        return items

    # post data to dynamodb 
    def post_data(email, firstname, lastname, password):
        put_data = table.put_item(

            Item = {
                    'Email' :  email,
                    'Firstname' : firstname,
                    'Lastname' : lastname,
                    'Password': password 
            }           
        )

        return put_data

