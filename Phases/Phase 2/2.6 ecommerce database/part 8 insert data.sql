-- USE ecommerce_db;

INSERT INTO categories (category_name)
VALUES
('Electronics'),
('Clothing'),
('Shoes'),
('Books'),
('Home & Kitchen');


INSERT INTO customers
(first_name, last_name, email, phone, password_hash)
VALUES
('Ali', 'Khan', 'ali.khan@example.com', '03001234567', 'hash_ali_123'),
('Ahmed', 'Raza', 'ahmed.raza@example.com', '03011234567', 'hash_ahmed_123'),
('Sara', 'Malik', 'sara.malik@example.com', '03121234567', 'hash_sara_123'),
('Hassan', 'Ali', 'hassan.ali@example.com', '03211234567', 'hash_hassan_123'),
('Ayesha', 'Shah', 'ayesha.shah@example.com', '03331234567', 'hash_ayesha_123'),
('Usman', 'Tariq', 'usman.tariq@example.com', '03451234567', 'hash_usman_123');


INSERT INTO addresses
(customer_id, address_line, city, postal_code, country)
VALUES
(1, '12 Model Town Road', 'Lahore', '54700', 'Pakistan'),
(1, '25 Johar Town Block H', 'Lahore', '54782', 'Pakistan'),
(2, '45 Gulshan-e-Iqbal Block 5', 'Karachi', '75300', 'Pakistan'),
(3, '18 F-8 Markaz', 'Islamabad', '44000', 'Pakistan'),
(4, '72 Cantt Road', 'Lahore', '54800', 'Pakistan'),
(5, '33 DHA Phase 5', 'Karachi', '75500', 'Pakistan'),
(6, '21 Satellite Town', 'Rawalpindi', '46300', 'Pakistan');


INSERT INTO products
(category_id, product_name, description, price, stock_quantity)
VALUES
(1, 'Dell Inspiron 15', '15-inch business laptop', 145000.00, 15),
(1, 'Logitech Wireless Mouse', 'Wireless optical mouse', 3500.00, 50),
(1, 'Mechanical Keyboard', 'RGB mechanical gaming keyboard', 8500.00, 30),
(1, 'Samsung 24-inch Monitor', 'Full HD LED monitor', 32000.00, 20),

(2, 'Men Cotton T-Shirt', 'Premium cotton t-shirt', 2500.00, 100),
(2, 'Women Casual Dress', 'Casual summer dress', 5500.00, 40),

(3, 'Nike Running Shoes', 'Lightweight running shoes', 18500.00, 25),
(3, 'Adidas Sneakers', 'Casual everyday sneakers', 15000.00, 35),

(4, 'Clean Code', 'Programming best practices book', 4500.00, 20),
(4, 'The Pragmatic Programmer', 'Software development book', 5000.00, 15),

(5, 'Non-Stick Frying Pan', '28cm non-stick frying pan', 4200.00, 25),
(5, 'Electric Kettle', '1.7L electric kettle', 6500.00, 18);


INSERT INTO orders
(customer_id, status)
VALUES
(1, 'Delivered'),
(2, 'Shipped'),
(3, 'Processing'),
(1, 'Pending'),
(4, 'Delivered'),
(5, 'Cancelled'),
(6, 'Delivered'),
(3, 'Pending');



INSERT INTO order_items
(order_id, product_id, quantity, unit_price)
VALUES
-- Order 1
(1, 1, 1, 145000.00),
(1, 2, 2, 3500.00),

-- Order 2
(2, 7, 1, 18500.00),
(2, 8, 1, 15000.00),

-- Order 3
(3, 3, 1, 8500.00),
(3, 4, 1, 32000.00),

-- Order 4
(4, 5, 3, 2500.00),

-- Order 5
(5, 9, 1, 4500.00),
(5, 10, 1, 5000.00),

-- Order 6
(6, 6, 1, 5500.00),

-- Order 7
(7, 11, 2, 4200.00),
(7, 12, 1, 6500.00),

-- Order 8
(8, 1, 1, 145000.00),
(8, 3, 1, 8500.00);




INSERT INTO payments
(order_id, payment_method, payment_status, amount)
VALUES
(1, 'Card', 'Paid', 152000.00),
(2, 'Online', 'Paid', 33500.00),
(3, 'Card', 'Paid', 40500.00),
(4, 'Cash', 'Pending', 7500.00),
(5, 'Bank Transfer', 'Paid', 9500.00),
(6, 'Card', 'Refunded', 5500.00),
(7, 'Cash', 'Paid', 14900.00),
(8, 'Online', 'Pending', 153500.00);