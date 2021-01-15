import pymongo
from pymongo import MongoClient


def mongo_get():
   client = MongoClient('localhost', 27017)
   db = client.people
   people = db.people
   alldata = list(people.find({}, {'_id': False}))
   print(type(alldata))
   print(str(alldata))
   print(client.list_database_names())
   return alldata

mongo_get()