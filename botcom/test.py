#!/usr/bin/python3
"""script that takes in an argument and displays all values
in the states able of hbtn_0e_0_usa where name matches
the argument"""


import MySQLdb


if __name__ == "__main__":

    try:
        db = MySQLdb.connect(
                host="localhost",
                user="root",
                password='',
                database="eshop",
                charset="utf8"
                )
        cur = db.cursor(dictionary=True)
        cur.execute("""
        SELECT *
        FROM product
        WHERE quantity_available > 0
        """)
        rows = cur.fetchall()
        for row in rows:
            print(f"Name - {row['product_name']}, About - {row['description']}, Price - ${row['price']}, Total - {row['quantity_available']}")

    except MySQLdb.Error as e:
        print(f"Error: {e}")
