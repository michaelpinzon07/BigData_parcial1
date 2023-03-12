

import json
import datetime
import boto3
import csv
from bs4 import BeautifulSoup

def poner_datos(event, context):
    s3 = boto3.resource('s3')
    # Leer el archivo del bucket "busquetsito"
    bucket_origen = s3.Bucket('bucketparcialmicha2')
    nuevo = event['Records'][0]['s3']['object']['key']
    obj = bucket_origen.Object(nuevo)
    obj = obj.get()['Body'].read().decode('utf-8')
    soup = BeautifulSoup(obj, 'html.parser')
    a = soup.find_all('script', {'type': 'application/ld+json'})
    a_lines = str(str(a).splitlines()[1:-1])
    a_lista_casas = [casa for casa in a_lines.split('image')[1:]]
    diccionario_casas = {}
    lista_info = []
    for casa in a_lista_casas:
        diccionario_casas['imagen'] ='https://' + casa.split('jpg')[0].split('https://')[1] + 'jpg'
        diccionario_casas['titulo'] = casa.split('"name": ')[1].split('"description": ')[0]
        diccionario_casas['descripcion'] = casa.split('"description": ')[1].split('",')[0]
        lista_info.append(diccionario_casas)

    # Escribir la info filtrada en el bucket "busquetsitofinal"
    bucket_destino = s3.Bucket('bucketparcialmicha2.1')
    actual = datetime.datetime.now()
    nombre = f"{actual.year}-{actual.strftime('%m')}-{actual.strftime('%d')}.txt"
    bucket_destino.put_object(Body=str(lista_info), Key=nombre)

    return {
        'statusCode': 200,
        'body': json.dumps('Finisimo')
    }