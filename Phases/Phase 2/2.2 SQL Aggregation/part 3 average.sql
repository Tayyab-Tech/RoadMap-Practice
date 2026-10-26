use orders_db;

-- select avg(quantity) as average_quantity from orders;

-- select round(avg(price),2) as average_price from orders;


SELECT round(avg(quantity*price),2) AS average_order_value
FROM orders;