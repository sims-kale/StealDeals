# myapp/tasks.py
import schedule
import time
# from .views import webscrape
from pymongo import MongoClient


def greet():
    client = MongoClient('localhost', 27017)
    
    buyzilla = client.buyzilla
    read = buyzilla.products.find({})
    # print("Hello, World!")
    for doc in read:
        print( doc)
    client.close()
   

schedule.every(20).seconds.do(greet)

while True:
    schedule.run_pending()
    time.sleep(1)
    
