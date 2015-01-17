from pymongo import MongoClient
import json

client = MongoClient()

db = client['vaccinfo']
schedule = db['schedule']
users = db['users']


if __name__ = '__main__':
	pass