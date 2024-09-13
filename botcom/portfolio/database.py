#!/usr/bin/env python3
"""Searching for uses on the database, if user exits
their  details is returned else the user is created"""

def search_user(phone_number):
    cursor = mysql.connection.cursor()
    
    # Query to check if the user exists in the database by phone number
    query = "SELECT id, name, email FROM users WHERE phone_number = %s LIMIT 1"
    cursor.execute(query, (phone_number,))
    user = cursor.fetchone()
    cursor.close()

    if user:
        return {
            'user_id': user[0],
            'name': user[1],
            'email': user[2]
        }
    else:
        return None  # User not found

# Function to save user details in the database
def create_user(name, email, phone_number):
    cursor = mysql.connection.cursor()
    
    # Query to insert user details into the users table
    query = "INSERT INTO users (name, email, phone_number) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, phone_number))
    mysql.connection.commit()
    
    # Get the newly created user ID
    user_id = cursor.lastrowid
    cursor.close()

    return user_id

