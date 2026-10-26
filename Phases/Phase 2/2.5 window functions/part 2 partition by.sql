USE window_functions_db;

SELECT
    employee_name,
    department,
    sales_amount,
    ROW_NUMBER() OVER (
        PARTITION BY department
        ORDER BY sales_amount DESC
    ) AS row_num
FROM sales;