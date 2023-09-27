import psycopg2
from os import getenv
import pandas as pd
from queries import DROP_CHARACTER_TABLE
from sqlite_example import connect_to_db,execute_q
#postgreSQL connection credentials

#user and default database
DBNAME = getenv("DBNAME")
USER = getenv("USER")

#password value
PASSWORD = getenv("PASSWORD") 

#server from SQL
HOST =  getenv("HOST")

def connect_to_pg(dbname = DBNAME,user = USER,password = PASSWORD,host = HOST):
    pg_conn = psycopg2.connect(dbname = DBNAME,user = USER,password = PASSWORD,host = HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs

def execute_q(conn,query):
    #make the cursor 
    curs = conn.cursor()
    #execute the query
    curs.execute(query)
    #pull the results
    return curs.fetchall()

def modify_db(conn,curs,query):
    results = curs.execute(query)
    conn.commit()
    return results

TITANIC_TABLE = """
    CREATE TABLE IF NOT EXISTS titanic_table(
        passenger_id SERIAL PRIMARY KEY,
        Survived INT NOT NULL,
        Pclass INT NOT NULL,
        Name VARCHAR(100) NOT NULL,
        Sex VARCHAR(10) NOT NULL,
        Age float NOT NULL,
        Siblings_Spouses_Aboard INT NOT NULL,
        Parents_Children_Aboard INT NOT NULL,
        Fare float NOT NULL
    )
"""

df = pd.read_csv("titanic.csv")

if __name__ == "__main__":

    pg_conn,pg_curs = connect_to_pg()
    
    #Create the table and its associated schema
    modify_db(pg_curs, pg_conn, DROP_CHARACTER_TABLE)
    modify_db(pg_curs, pg_conn, TITANIC_TABLE)

    records = df.values.tolist()

    for record in records:
        insert_statement ="""
            INSERT INTO titanic_table ("Survived","Pclass","Name","Sex","Age",
            "Siblings_Spouses_Aboard","Parents_Children_Aboard","Fare")
            VALUES = {};
            """.format(tuple(record))
        modify_db(pg_curs, pg_conn, insert_statement)
