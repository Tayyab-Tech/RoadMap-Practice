-- SELECT
--     category,
--     COUNT(*) AS total_orders
-- FROM orders
-- GROUP BY category
-- HAVING COUNT(*) > 2;



-- SELECT
--     category,
--     SUM(quantity * price) AS total_revenue
-- FROM orders
-- GROUP BY category
-- HAVING SUM(quantity * price) > 2000;




-- SELECT
--     category,
--     round(AVG(price),2) AS average_price
-- FROM orders
-- GROUP BY category
-- HAVING AVG(price) > 500;




-- Question: Find categories with completed orders whose revenue exceeds 1,000.


SELECT
    category,
    SUM(quantity * price) AS total_revenue
FROM orders
WHERE status = 'Completed'
GROUP BY category
HAVING SUM(quantity * price) > 1000;