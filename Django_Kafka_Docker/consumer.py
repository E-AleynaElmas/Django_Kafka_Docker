"""
    kafkadaki verilerin mongodb ye kaydı
"""

from kafka import KafkaConsumer
import pymongo
import json


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myDatabase"]
mycol = mydb["logs"]


consumer = KafkaConsumer(
    'logs2',
    group_id='my-group',
    client_id="my_py_id",
    bootstrap_servers=["localhost:9092"])


for message in consumer:
    mydict = { "log": message.value.decode() }
    x = mycol.insert_one(mydict)