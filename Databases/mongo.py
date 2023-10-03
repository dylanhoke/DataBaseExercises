import pymongo
import dnspython
from queries import GET_CHARACTERS
from sqlite_example import connect_to_db,execute_q


DBNAME = "test" 
PASSWORD = "password"

#how are request will come back from sequel lite
test_characters = [
    (1,"name",0,0),
    (2,"name2",0,0)
]


#how are data will be stored inside of mongodb
character_documents = [
    {
        "character_1": 1,
        "name":, 
        "exp":,
        "stats":
    }
    {
        "character_2": 2,
        "name":, 
        "exp":,
        "stats":  
    }
]

#credentials
def mongo_connect(password=PASSWORD, dbname=DBNAME, collection_name="characters"):
    client = pymongo.MongoClient(f"key{PASSWORD},{DBNAME}")
    db=client[dbname]
    collection=db[collection_name]
    return collection

if __name__ == "__main__":
    sl_conn = connect_to_db()
    sl_characters = execute_q(sl_conn,GET_CHARACTERS)

    #connect to a collection
    collection=mongo_connect(collection_name="people")


    for character in sl_characters:
        doc = {
            "character_1": character[0],
            "name": character[1],
            "exp": character[2],
            "stats": character[3]
        }
        collection.insert_one(doc)
    
    
    #result=collection.find_one({"name":"Dylan"})
    #print(result)
