from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://root:root@mycluster.jtujc9h.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster"
# Create a new client and connect to the server
client = MongoClient(uri)

db = client.todo_db

collection_name = db["todo_collection"]






'''
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
'''