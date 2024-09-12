from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'eshop'

mysql = MySQL(app)

@app.route('/botcom', methods=['POST'])
def botcom():
    incoming_msg = request.values.get('Body', '').lower()
    phone_number = request.values.get('From', '').strip()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hello' in incoming_msg or 'hi' in incoming_msg:
        msg.body("hello, how my I help you today?")
    if 'browse products' in incoming_msg or 'show goods' in incoming_msg:
        cursor = mysql.connection.cursor()

        cursor.execute("SELECT * FROM product WHERE quantity_available > 0")
        products = cursor.fetchall()
        if products:
            product_list = "Here are availlable products:\n"
            for prod in products:
                product_list += f"Name: {prod[0]}, About: {prod[1]}, Price: ${prod[2]}, Quantity: {prod[3]}" 
                msg.body(product_list)
        else:
            msg.body("There are no availlable products at the moment")
    else:
        msg.body("Sorry I did not understand that")
    return str(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

