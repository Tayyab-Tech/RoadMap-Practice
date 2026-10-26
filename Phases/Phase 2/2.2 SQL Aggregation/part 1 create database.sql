-- Create Database
CREATE DATABASE orders_db;

-- Select Database
USE orders_db;

-- Create Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer VARCHAR(100) NOT NULL,
    category VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
	quantity INT NOT NULL,
	price DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL
);

-- Insert Sample Data
INSERT INTO orders 
(order_id, customer, category, city, quantity, price, status)
VALUES
(1, 'Ali', 'Electronics', 'Lahore', 2, 500, 'Completed'),
(2, 'Sara', 'Clothing', 'Karachi', 3, 100, 'Completed'),
(3, 'Hamza', 'Electronics', 'Lahore', 1, 700, 'Pending'),
(4, 'Ayesha', 'Furniture', 'Islamabad', 2, 300, 'Completed'),
(5, 'Bilal', 'Clothing', 'Lahore', 4, 100, 'Completed'),
(6, 'Zain', 'Electronics', 'Karachi', 3, 400, 'Completed'),
(7, 'Hina', 'Furniture', 'Lahore', 1, 800, 'Pending'),
(8, 'Usman', 'Clothing', 'Islamabad', 2, 200, 'Completed');



-- Add Revenue column
ALTER TABLE orders
ADD COLUMN revenue DECIMAL(10, 2);

-- Calculate and store revenue
UPDATE orders
SET revenue = quantity * price
where order_id > 0;

-- Check the result
SELECT * FROM orders;