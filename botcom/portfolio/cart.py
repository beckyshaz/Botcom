#!/usr/bin/env python3
"""creating carts for users if cart does not exist
if it exists we add item to cart"""

from portfolio.bot import mysql

def add_product_to_cart(user_id, product_id, quantity):
    cursor = mysql.connection.cursor()

    # Check if the user already has a cart
    query = "SELECT cart_id FROM cart WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    cart = cursor.fetchone()

    if cart:
        cart_id = cart.get('cart_id')

    print("DEBUG: Cart fetched:", cart)

    if not cart:
        # If the user doesn't have a cart, create one
        query = "INSERT INTO cart (user_id) VALUES (%s)"
        cursor.execute(query, (user_id,))
        mysql.connection.commit()

        # Get the cart ID of the newly created cart
        cart_id = cursor.lastrowid
    else:
        # Use the existing cart ID
        cart_id = cart['cart_id']

        #Insert the product into the cartitem table
        query_insert_cartitem = """
        INSERT INTO cartitem (cart_id, product_id, quantity)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query_insert_cartitem, (cart_id, product_id, quantity))
        mysql.connection.commit()
        cursor.close()
