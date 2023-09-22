"""
Beginning SQL
"""
import sqlite3
import queries as q

# Step 1
# Connect to the database - check your spelling!
connection = sqlite3.connect("rpg_db.sqlite3")


# Step 2
# The teller will travel to the DB and pull information out
cursor = connection.cursor()


# Step 3 - write a query - (See the queries.py file)
#change

# Step 4 - Execute the query on the cursor and fetch the results
#"pulling the results from the cursor"
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == "__main__":
    print(results[:5])