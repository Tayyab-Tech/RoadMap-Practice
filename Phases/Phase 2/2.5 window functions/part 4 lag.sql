USE window_functions_db;

-- SELECT
--     sale_date,
--     sales_amount,
--     LAG(sales_amount) OVER (
--         ORDER BY sale_date
--     ) AS previous_sales
-- FROM sales;


SELECT
    sale_date,
    sales_amount,

    LAG(sales_amount) OVER (
        ORDER BY sale_date
    ) AS previous_sales,

    sales_amount -
    LAG(sales_amount) OVER (
        ORDER BY sale_date
    ) AS sales_change

FROM sales;