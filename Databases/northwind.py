from queries import EXPENSIVE_ITEMS
import sqlite3

def connect_to_db(dbname = "northwind_small.sqlite3"):
    return sqlite3.connect(dbname)

def execute_query(conn,query):
    #make the cursor 
    curs = conn.cursor()
    #execute the query
    curs.execute(query)
    #pull the results
    conn.commit()

if __name__ == "__main__":
    conn = connect_to_db()
    execute_query(conn,EXPENSIVE_ITEMS)