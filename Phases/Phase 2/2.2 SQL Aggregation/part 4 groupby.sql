-- SELECT category, COUNT(*) AS total_orders
-- FROM orders
-- GROUP BY category;



-- SELECT
--     category,
--     SUM(quantity) AS total_items
-- FROM orders
-- GROUP BY category;



-- SELECT
--     category,
--     round(AVG(price),2) AS average_price
-- FROM orders
-- GROUP BY category;




SELECT
    category,
    COUNT(*) AS total_orders,
    SUM(quantity) AS total_items,
    round(AVG(price),2) AS average_price,
    SUM(quantity * price) AS total_revenue
FROM orders
GROUP BY category;