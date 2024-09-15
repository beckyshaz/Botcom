#!/usr/bin/env python3
"""quering database to check if the product requested by the
user exists"""

from portfolio.bot import mysql

def search_product(product_name):
    cursor = mysql.connection.cursor()

    query = "SELECT product_id, product_name, price, quantity_available FROM product WHERE product_name LIKE %s LIMIT 1"

    cursor.execute(query, (product_name,))

    # Fetch the first matching product
    product_data = cursor.fetchone()
    cursor.close()
    print(product_data)

    if product_data:
        return {
                'product_id': product_data['product_id'],
                'product_name': product_data['product_name'],
                'price': product_data['price'],
                'stock': product_data['quantity_available']
                }
    else:
        return None
