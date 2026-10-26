-- use company_employees;
-- CASE
--     WHEN condition THEN result
--     WHEN condition THEN result
--     ELSE result
-- END


-- SELECT
--     employee_name,
--     salary,
--     CASE
--         WHEN salary >= 100000 THEN 'High'
--         WHEN salary >= 60000 THEN 'Medium'
--         ELSE 'Low'
--     END AS salary_level
-- FROM employees;


-- Case with aggregation

-- SELECT
--     COUNT(CASE WHEN salary >= 100000 THEN 1 END) AS high_salary,
--     COUNT(CASE WHEN salary >= 60000
--                AND salary < 100000 THEN 1 END) AS medium_salary,
--     COUNT(CASE WHEN salary < 60000 THEN 1 END) AS low_salary
-- FROM employees;




-- case with order by
-- use employeedata;
-- SELECT
--     name,
--     department,
--     salary
-- FROM employee
-- ORDER BY
--     CASE
--         WHEN department = 'IT' THEN 1
--         WHEN department = 'Sales' THEN 2
--         WHEN department = 'Finance' THEN 3
--         ELSE 4
--     END;
