from flask import Flask, request
from flask import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/botcom', methods=['POST'])
def botcom():
    incoming_msg = request.values.get('Body', '').lower()
    phone_number = request.values.get('From', '').strip()
    resp = MessagingResponse()
    msg = resp.message()











if __name__ == '__main__':
    app.run(port=5000)

