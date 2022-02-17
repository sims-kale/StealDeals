from pymongo import MongoClient
import pprint

def writeIntoDatabase(amz,flip, aprice, fprice):
    client = MongoClient('localhost', 27017)
    buyzilla = client.buyzilla
    print("Connection Successfully")
    # client.close()
    buyzilla.products.insert_one({"amazon":amz,"amazon":aprice,"flipkart":flip, "flipkart":fprice})
    print("Inserted successfully")
    pprint.pprint(buyzilla.products.find())
    print(amz,flip)

