USE orders_db;

-- SELECT SUM(quantity) AS total_items
-- FROM orders;

-- SELECT SUM(quantity * price) AS total_revenue
-- FROM orders;

SELECT 
    SUM(quantity) AS total_quantity,
    SUM(price) AS total_price,
    SUM(quantity * price) AS total_revenue
FROM orders;
