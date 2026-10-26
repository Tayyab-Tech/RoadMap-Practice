USE window_functions_db;

-- SELECT
--     employee_name,
--     sales_amount,
--     RANK() OVER (
--         ORDER BY sales_amount DESC
--     ) AS sales_rank
-- FROM sales;


SELECT
    employee_name,
    department,
    sales_amount,
    RANK() OVER (
        PARTITION BY department
        ORDER BY sales_amount DESC
    ) AS department_rank
FROM sales;