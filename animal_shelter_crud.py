from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    # The user and password are initialized with default values for backwards compatibility with crud_test.py, but accept new values for Module 5
    def __init__(self, user = 'aacuser', passw = '4444'):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection Variables
        #
        self.user = user
        self.passw = passw
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30798
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (self.user,self.passw,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data)  # data should be dictionary            
            return result.acknowledged
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        return false

# Create method to implement the R in CRUD.
    def query(self, data):
        if data is not None:
            result = list(self.database.animals.find(data))
            return result
        else:
            raise Exception("Empty data argument")
        return []

# Update method to change values stored in documents
    def update(self, query_data, update_data):
        if query_data is not None and update_data is not None:
            return self.database.animals.update_many(query_data, {"$set": update_data}).modified_count
        else:
            raise Exception("Invalid data arguments")
        return 0

# Delete method to remove documents from the database
    def delete(self, data):
        if data is not None:
            return self.database.animals.delete_many(data).deleted_count
        else:
            raise Exception("Invalid data argument")
        return 0

# Implement a specialized read method for Mod 6 that returns all documents if the argument is empty, but passes to query otherwise
    def read(self, query_data):
        if query_data is None:
            return self.database.animals.find()
        else:
            return self.query(query_data)
        return []
