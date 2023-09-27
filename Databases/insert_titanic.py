import psycopg2
from os import getenv
import pandas as pd

#postgreSQL connection credentials

DBNAME = getenv("DBNAME")
USER = getenv("USER")
PASSWORD = getenv("PASSWORD")
HOST = getenv("HOST")

pg_conn = psycopg2.connect(dbname = DBNAME, user = USER, password = PASSWORD, host = HOST)
pg_curs = pg_conn.cursor()

def execute_query_pg(curs,conn,query):
    results = curs.execute(query)
    conn.commit()
    return results

CREATE_TITANIC_TABLE = """
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
    );
"""

DROP_TITANIC_TABLE = """
    DROP TABLE IF EXISTS titanic_table;
"""

df = pd.read_csv("titanic.csv")
df["Name"] = df["Name"].str.replace("'",'')

if __name__ == "__main__":

    #Create the table and its associated schema
    execute_query_pg(pg_curs, pg_conn, DROP_TITANIC_TABLE)
    execute_query_pg(pg_curs, pg_conn, CREATE_TITANIC_TABLE)

    records = df.values.tolist()

    for record in records:
        insert_statement ="""
            INSERT INTO titanic_table (Survived,Pclass,Name,Sex,Age,
            Siblings_Spouses_Aboard,Parents_Children_Aboard,Fare)
            VALUES {};
            """.format(tuple(record))
        execute_query_pg(pg_curs, pg_conn, insert_statement)
