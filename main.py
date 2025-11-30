from pymongo import MongoClient
from functions import *

client = MongoClient('mongodb://localhost:27017')
db = client.get_database('lista-tarefas')
colecao = db.get_collection('tarefas')


menu(colecao)

tarefas = list(colecao.find())
if tarefas:
    for t in tarefas:
        print(f"Encontrei: {t['titulo']}")
else:
    print("Realmente, a coleção está vazia.")