USE orders_db;
-- SELECT COUNT(*) as total_orders
-- FROM orders;

-- SELECT COUNT(distinct price) AS price
-- FROM orders;

SELECT COUNT(DISTINCT city) AS total_cities
FROM orders;