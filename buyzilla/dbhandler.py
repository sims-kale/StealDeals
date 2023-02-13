from pymongo import MongoClient
import pprint


def writeIntoDatabase( aproduct, fproduct):
    client = MongoClient('localhost', 27017)
    buyzilla = client.buyzilla
    # 
    # print("Connection Successfully")

    buyzilla.products.insert_one(
        {
            
            "amz_product": aproduct, "flip_product": fproduct,
            
            
        })
    # print("Inserted successfully")
    # readIntoDatabase()


def readIntoDatabase():
    client = MongoClient('localhost', 27017)
    buyzilla = client.buyzilla
    read = buyzilla.products.find({})
    # for doc in read:
        # print( doc)
    # client.close()
    return read
