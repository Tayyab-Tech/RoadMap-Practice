use company_employees;

-- SELECT employee_name, salary
-- FROM employees
-- WHERE salary > (
--     SELECT AVG(salary)
--     FROM employees
-- );

-- Types of Subqueries

-- A. Scalar subquery
-- Returns one value.

-- SELECT employee_name, salary
-- FROM employees
-- WHERE salary > (
--     SELECT AVG(salary)
--     FROM employees
-- );

-- avg() gives one value 



-- B. Subquery with IN

SELECT employee_name
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM departments
    WHERE department_name = 'IT'
);
