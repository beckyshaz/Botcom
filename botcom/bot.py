from flask import Flask, request
from flask import requests
from twilio.twiml.messaging_response import MessagingResponse
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['PASSWORD'] = ''
app.config['DATABASE'] = 'eshop'

mysql = MySQL(app)

@app.route('/botcom', methods=['POST'])
def botcom():
    incoming_msg = request.values.get('Body', '').lower()
    phone_number = request.values.get('From', '').strip()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hello' or 'hi' in incoming_msg:
        msg.body = "hello, how my I help you today?"
    if 'browse products' or 'show goods' in incoming_msg:
        cursor = mysql.connection.cursor()

        cursor.execute(("SELECT * FROM product WHERE quantity_available > 0")









if __name__ == '__main__':
    app.run(port=5000)

