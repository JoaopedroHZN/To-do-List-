from pymongo import MongoClient
from functions import *

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.get_database('lista-tarefas')
colecao = db.get_collection('tarefas')



menu()