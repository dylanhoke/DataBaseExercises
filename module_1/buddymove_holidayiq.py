import pandas as pd
import sqlite_example
import sqlite3
import queries as q


df = pd.read_csv("buddymove_holidayiq.csv")
conn = sqlite3.connect("buddymove_holidayiq.sqlite3")
df.to_sql("review",conn,if_exists = "replace",index = False)

def connect_to_db(db_name="buddymove_holidayiq.sqlite3"):
    return sqlite3.connect(db_name)


def execute_q(conn,query):
    #make the cursor 
    curs = conn.cursor()
    #execute the query
    curs.execute(query)
    #pull the results
    return curs.fetchall()


if __name__ == "__main__":
    conn = connect_to_db()
    results = execute_q(conn,q.AVG_ITEM_WEIGHT_PER_CHARACTER)
    df = pd.DataFrame(results)