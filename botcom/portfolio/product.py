#!/usr/bin/env python3
if __name__ == "__main__":
    """quering database to check if the product requested by the
    user exists"""

    def search_product(product_name):
        cursor = mysql.connection.cursor()

        query = "SELECT product_id, product_name, price, quantity_available FROM product WHERE name LIKE %s LIMIT 1"
        cursor.execute(query, (product_name))

        # Fetch the first matching product
        product = cursor.fetchone()
        cursor.close()

        if product:
            return {
                    'product_id': product[0],
                    'product_name': product[1],
                    'price': product[2],
                    'quantity_available': product[3]
                    }
        else:
            return None
