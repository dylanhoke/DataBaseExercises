"""
Beginning SQL
"""
import sqlite3
import queries as q

#DB Connect function
def connect_to_db(db_name="rpg_db.sqlite3"):
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
    print(execute_q(conn,q.SELECT_ALL)[:5])

# # Step 1
# # Connect to the database - check your spelling!
# connection = sqlite3.connect("rpg_db.sqlite3")


# # Step 2
# # The teller will travel to the DB and pull information out
# cursor = connection.cursor()


# # Step 3 - write a query - (See the queries.py file)
# #change

# # Step 4 - Execute the query on the cursor and fetch the results
# #"pulling the results from the cursor"
# results = cursor.execute(q.SELECT_ALL).fetchall()
