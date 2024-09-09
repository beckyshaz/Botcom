-- creating a database using create database
CREATE DATABASE IF NOT EXISTS eshop;
USE eshop;

CREATE TABLE IF NOT EXISTS users(
first_name VARCHAR(50) NOT NULL,
second_name VARCHAR(50) NOT NULL,
username VARCHAR(50) NOT NULL,
email VARCHAR(100) NOT NULL,
password_hash VARCHAR(255) NOT NULL,
phone_number VARCHAR(100),
PRIMARY KEY (phone_number),
UNIQUE (username),
UNIQUE (email)
);

CREATE TABLE IF NOT EXISTS product (
	product_id INT AUTO_INCREMENT PRIMARY KEY,
	product_name VARCHAR(255),
	description TEXT,
	price DECIMAL(10, 2),
	quantity_available INT
);

CREATE TABLE IF NOT EXISTS cart (
	cart_id INT AUTO_INCREMENT PRIMARY KEY,
	phone_number VARCHAR(100),
	total_amount DECIMAL (10, 2),
	FOREIGN KEY (phone_number) REFERENCES users(phone_number) ON DELETE CASCADE	
);

CREATE TABLE IF NOT EXISTS cartitem (
	cartitem_id INT AUTO_INCREMENT PRIMARY KEY,
	cart_id INT,
	product_id INT,
	quantity INT,
	price DECIMAL(10, 2),
	FOREIGN KEY (cart_id) REFERENCES cart(cart_id) ON DELETE CASCADE,
	FOREIGN KEY (product_id) REFERENCES product(product_id) ON DELETE CASCADE
);


INSERT INTO product (product_name, description, price, quantity_available)
VALUES
    ('Smartphone A', 'Very smart and easy to use phone', 19.99, 50),
    ('Smartphone B', 'Unique and waterproof', 20.99, 100),
    ('Headphones B', 'Protects your eardrum', 5.00, 1000),
    ('Television C', 'Smart LED TVs', 300.00, 1000),
    ('Computer D', 'High performing computers', 400.00, 1000);

