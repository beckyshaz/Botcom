from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask_mysqldb import MySQL
from portfolio import database.py

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'eshop'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/botcom', methods=['POST'])
def botcom():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hello' in incoming_msg.lower() or 'hi' in incoming_msg.lower():
        msg.body("Hello, How may I help you Today?")
    elif 'browse products' in incoming_msg.lower() or 'show me products' in incoming_msg.lower():
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
        name = f'{user["name"]}'
        if user:
            msg.body(name 'Welcome back, Please provide name of product and quantity, e.g, smartphoneA 2')
            product_quantity = incoming_msg.lower().split()
            if len product_quantity == 2:
                product_name = product_quantity[0]
                quantity = product_quantity[1]
                if isdigit(quantity):
                    quantity = int(quantity)
                else:
                    msg.body('Provide a number for quantity of products You want')
            else:
                msg.body('Please, provide product name and quantity, e.g., "smartphoneA 2"')
    else:
        msg.body("Sorry, I did not understand that")

    return str(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

