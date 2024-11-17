from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://isprojectmit2024:NbedSBMCTUiiohtm@cluster0.cyqjo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client['userdata']
collections = db.list_collection_names()

print("Collections in the database");

for collection in collections:
    print(collection)



new_collection = db["test"]
document1 = {
    'name' : 'Alice',
    'age' : 10

}
new_collection.insert_one(document1)
collections = db.list_collection_names()

print("Collections in the database");

for collection in collections:
    print(collection)



client.close()
