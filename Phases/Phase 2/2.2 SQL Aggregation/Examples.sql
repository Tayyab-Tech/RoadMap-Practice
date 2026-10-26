-- SELECT
--     COUNT(*) AS total_orders,
--     SUM(quantity) AS total_items,
--     AVG(quantity * price) AS average_order_value,
--     SUM(quantity * price) AS total_revenue
-- FROM orders;


-- SELECT
--     city,
--     COUNT(*) AS total_orders,
--     SUM(quantity * price) AS total_revenue
-- FROM orders
-- GROUP BY city
-- ORDER BY total_revenue DESC;



-- SELECT
--     category,
--     COUNT(*) AS completed_orders,
--     SUM(quantity * price) AS revenue
-- FROM orders
-- WHERE status = 'Completed'
-- GROUP BY category
-- ORDER BY revenue DESC;




-- SELECT
--     category,
--     SUM(quantity * price) AS total_revenue
-- FROM orders
-- GROUP BY category
-- HAVING SUM(quantity * price) > 1000
-- ORDER BY total_revenue DESC;


SELECT
    city,
    category,
    COUNT(*) AS total_orders,
    SUM(quantity * price) AS total_revenue
FROM orders
GROUP BY city, category
ORDER BY city, total_revenue DESC;