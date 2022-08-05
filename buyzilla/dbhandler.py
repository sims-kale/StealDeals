from pymongo import MongoClient
import pprint

def writeIntoDatabase(amz_link,flip_link,aprice,fprice):
    client = MongoClient('localhost', 27017)
    buyzilla = client.buyzilla
    print("Connection Successfully")
   
    buyzilla.products.insert_one({"amz_link":amz_link,"flip_link":flip_link,"amzon":aprice,"flipkart":fprice})
    print("Inserted successfully")
    # pprint.pprint(buyzilla.products.find())
    print(amz_link,flip_link)
    readIntoDatabase()


def readIntoDatabase():
    client = MongoClient('localhost', 27017)
    buyzilla = client.buyzilla
    read= buyzilla.products.find({})
    for doc in read:
        print(doc)

    # client.close()

