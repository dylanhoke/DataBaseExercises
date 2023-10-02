from queries import CREATE_DEMO_TABLE,INSERT_DEMO
import sqlite3

def connect_to_db(dbname = "demo_data.sqlite3"):
    return sqlite3.connect(dbname)

def execute_query(conn,query):
    #make the cursor 
    curs = conn.cursor()
    #execute the query
    curs.execute(query)
    #pull the results
    conn.commit()

row_count = 3

xy_at_least_5 = 2

unique_y = 2

if __name__ == "__main__":
    conn = connect_to_db()
    execute_query(conn, CREATE_DEMO_TABLE)
    execute_query(conn, INSERT_DEMO)