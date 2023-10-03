import sqlite3


def connect_to_db(dbname="northwind_small.sqlite3"):
    return sqlite3.connect(dbname)


def execute_query(conn, query):

    curs = conn.cursor()
    curs.execute(query)
    conn.commit()


expensive_items = """
    SELECT * FROM Product
    ORDER BY UnitPrice DESC
    LIMIT 10;
"""

ADD_AGE = """
    ALTER TABLE Employee
    ADD Age INT;
"""

AGE_SOLVE = """
    UPDATE Employee
    SET Age =
    CAST(SUBSTRING(HireDate,1,4)AS HD)-CAST(SUBSTRING(BirthDate,1,4)
    AS BD)
"""

avg_hire_age = """
    SELECT AVG(HireDate - BirthDate) FROM Employee
"""

ten_most_expensive = """
    SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
    FROM Product, Supplier
    WHERE Product.SupplierId = Supplier.Id
    ORDER BY Product.UnitPrice DESC
    LIMIT 10;
"""

largest_category = """
    SELECT c.CategoryName, COUNT(DISTINCT p.Id) FROM Category c, Product p
    WHERE c.Id = p.CategoryId
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 1;
"""

if __name__ == "__main__":
    conn = connect_to_db()
