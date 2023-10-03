import sqlite3


def connect_to_db(dbname="demo_data.sqlite3"):
    return sqlite3.connect(dbname)


def execute_query(conn, query):

    curs = conn.cursor()
    curs.execute(query)
    conn.commit()


CREATE_DEMO_TABLE = """
    CREATE TABLE IF NOT EXISTS demo
    (
        "S" CHAR NOT NULL,
        "X" INT NOT NULL,
        "Y" INT NOT NULL
    );
"""

INSERT_DEMO = """
    INSERT INTO demo ("S", "X", "Y")
    VALUES
        ('g', 3, 9),
        ('v', 5, 7),
        ('f', 8, 7);
"""

row_count = """
    SELECT COUNT(*)
    FROM demo
"""

xy_at_least_5 = """
    SELECT COUNT(*) FROM demo
    WHERE X >=5 AND Y >=5
"""

unique_y = """
    SELECT COUNT(DISTINCT Y) FROM demo
"""

if __name__ == "__main__":
    conn = connect_to_db()
    execute_query(conn, CREATE_DEMO_TABLE)
    execute_query(conn, INSERT_DEMO)
