CREATE DATABASE window_functions_db;
USE window_functions_db;
CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department VARCHAR(50),
    sale_date DATE,
    sales_amount DECIMAL(10,2)
);
INSERT INTO sales
(sale_id, employee_name, department, sale_date, sales_amount)
VALUES
(1, 'Ali', 'Electronics', '2026-01-01', 50000),
(2, 'Ahmed', 'Electronics', '2026-01-05', 70000),
(3, 'Sara', 'Electronics', '2026-01-10', 60000),
(4, 'Hamza', 'Electronics', '2026-01-15', 70000),

(5, 'Ayesha', 'Clothing', '2026-01-02', 40000),
(6, 'Bilal', 'Clothing', '2026-01-07', 55000),
(7, 'Usman', 'Clothing', '2026-01-12', 45000),
(8, 'Hina', 'Clothing', '2026-01-18', 60000),

(9, 'Zain', 'Furniture', '2026-01-03', 80000),
(10, 'Maha', 'Furniture', '2026-01-08', 65000),
(11, 'Omar', 'Furniture', '2026-01-13', 80000),
(12, 'Noor', 'Furniture', '2026-01-20', 90000);


SELECT * FROM sales;