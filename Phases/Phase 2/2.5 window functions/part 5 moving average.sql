USE window_functions_db;


SELECT
    sale_date,
    sales_amount,

    AVG(sales_amount) OVER (
        ORDER BY sale_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg

FROM sales;