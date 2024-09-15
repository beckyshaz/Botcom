from flask import Flask, request, session
import secrets
from twilio.twiml.messaging_response import MessagingResponse
from flask_mysqldb import MySQL
from portfolio import database, product, cart

app = Flask(__name__)


app.secret_key = secrets.token_hex(16)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'eshops'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/botcom', methods=['POST'])
def botcom():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hello' in incoming_msg.lower() or 'hi' in incoming_msg.lower():
        msg.body("Hello, How may I help you Today?")
    elif 'browse products' in incoming_msg.lower() or 'show me available products' in incoming_msg.lower():
        cursor = mysql.connection.cursor()

        cursor.execute("SELECT product_name, price FROM product WHERE quantity_available > 0")
        products = cursor.fetchall()
        if products:
            product_list = ('Here are availlable products:\n')
            product_list += ('Name\t\t\t\tPrice\n')
            for prod in products:
                product_list += f'{prod["product_name"]}\t\t\t${prod["price"]}\n'
            msg.body(product_list)
        else:
            msg.body("There are no availlable products at the moment")

    elif 'add items to cart' in incoming_msg.lower():
        phone_number = request.values.get('From', '').strip()
        user = database.search_user(phone_number)
        if user:
            message = f'Welcome back {user["name"],}\n'
            message += 'Please provide name of product and quantity, e.g, "smartphoneA 2"'
            msg.body(message)
            product_quantity = incoming_msg.lower().split()
            if len(product_quantity) == 2:
                quantity = product_quantity[1]
                if isdigit(quantity):
                    quantity = int(quantity)
                else:
                    msg.body("Please, provide a digit as the quantity of products You want")
                product_name = product_quantity[0]
                product = search_product(product_name)
                if product:
                    user_id = user["user_id"]
                    add_product_to_cart(user_id, product['product_id'], quantity)
                    msg.body(f'{quantity} {product["product_name"]}(s) have been added to your cart.')
                else:
                    msg.body('Sorry, The product you requested is not available at the moment')
            else:
                msg.body('Please, provide product name and quantity, e.g., "smartphoneA 2"')
        else:
            message = 'I don’t have your details yet.\n Please provide your name and email.\n'
            message += 'First_name, second_name, email e.g\n'
            message += 'Walle, Walter, walewalter@gmail.com'
            msg.body(message)
            session['awaiting_details'] = True
            if session.get('awaiting_details'):
                user_details = incoming_msg.lower().split(',')
                if len(user_details) == 2:
                    first_name = user_details[0].strip()
                    second_name = user_details[1].strip()
                    email = user_details[2].strip()
                    user_id = create_user(first_name, second_name, email, phone_number)
                    msg = 'Thank you, your details have been added successfully\n'
                    msg += 'Now Please, provide the name of product and quantity to add to cart\n'
                    msg += 'Provide product name and quantity, e.g., "smartphoneA 2"\n'
                    msg.body(msg)
                    add_product_to_cart(user_id, product['product_id'], quantity)
                    msg.body(f'{quantity} {product["product_name"]}(s) have been added to your cart.')
            else:
                msg.body('Please, provide first_name, second_name and email')
    else:
        msg.body("Sorry, I did not understand that")

    return str(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

