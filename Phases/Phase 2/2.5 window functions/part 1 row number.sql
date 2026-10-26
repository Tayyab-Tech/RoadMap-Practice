USE window_functions_db;
select * from sales;
-- SELECT
--     employee_name,
--     sales_amount,
--     ROW_NUMBER() OVER (
--         ORDER BY sales_amount DESC
--     ) AS row_num
-- FROM sales;