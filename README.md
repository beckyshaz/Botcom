BotCom
Your WhatsApp E-commerce Assistant

Introduction
BotCom is a WhatsApp chatbot designed to enhance the shopping experience for users on e-commerce platforms. The bot allows customers to create accounts, browse products, add items to their cart. With seamless WhatsApp integration, BotCom brings the online shopping experience directly into users' favorite messaging app.

Deployed Site
Check out the live version of BotCom: Live URL https://suited-eager-bluejay.ngrok-free.app/botcom

Final Project Blog
Read the detailed blog post about the development of BotCom: Project Blog Article

Author
LinkedIn: https://www.linkedin.com/in/sharon-saka-88ba52254/

Installation
To run the project locally, follow these steps:

Clone the repository:

git clone https://github.com/beckyshaz/BotCom

Change into the project directory:
cd BotCom, cd botcom
Set up a virtual environment and activate it:

python3 -m venv botcom
source botcom/bin/activate  # On Windows use `botcom\Scripts\activate`
Install the dependencies:

pip install twilio flask

Run the application:

python3 -m portfolio.bot
For WhatsApp integration, set up your Twilio sandbox and configure the webhook URL:
You need to sign in and create account in ngrok
https://your-ngrok-url.com/botcom
Usage
Once the app is deployed, users can interact with the bot by sending a WhatsApp message to the Twilio Sandbox number using the code join applied-exercise.

Features:
User Registration: Collect user details like name, email, and phone number.
Browse Products: Display a list of available products with images.
Add to Cart: Users can add products to their cart, which is linked to their account.


Contributing
We welcome contributions to enhance BotCom. To contribute:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.

Related Projects
Twilio WhatsApp API
Flask Documentation

Licensing
This project is licensed under the MIT License. See the LICENSE file for more details
