



import requests
import random
#beatifoul soup
import boto3
import json
import datetime

def peticion():
    user_agents_list = [
        'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',   
    ]
    r = requests.get('https://homes.mitula.com/searchRE/q-chapinero', headers={'User-Agent': random.choice(user_agents_list)})
    soup = r.text
    return soup

    
    
def app(event, context):
    datos = peticion()
    actual = datetime.datetime.now()
    nombre = f"{actual.year}-{actual.strftime('%m')}-{actual.strftime('%d')}.txt"
    s3 = boto3.resource('s3')
    actual = datetime.datetime.now()
    nombre = f"{actual.year}-{actual.strftime('%m')}-{actual.strftime('%d')}.txt"
    bucket = s3.Bucket('bucketparcialmicha2')
    print('Se conecto al bucket')
    bucket.put_object(Key=nombre, Body=datos)
    return {
        'statusCode': 200,
        'body': json.dumps('Se guardan los datos')
    }