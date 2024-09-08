-- creating a database using create database
CREATE DATABASE IF NOT EXISTS shop;
USE shop;

CREATE TABLE IF NOT EXISTS users(
id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
second_name VARCHAR(50) NOT NULL,
username VARCHAR(50) NOT NULL,
email VARCHAR(100) NOT NULL,
password_hash VARCHAR(255) NOT NULL,
phone_number VARCHAR(100),
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
	id INT,
	total_amount DECIMAL (10, 2),
	FOREIGN KEY (id) REFERENCES users(id)	
);

CREATE TABLE IF NOT EXISTS cartitem (
	cartitem_id INT AUTO_INCREMENT PRIMARY KEY,
	cart_id INT,
	product_id INT,
	quantity INT,
	price DECIMAL(10, 2),
	FOREIGN KEY (cart_id) REFERENCES cart(cart_id),
	FOREIGN KEY (product_id) REFERENCES product(product_id)
);

