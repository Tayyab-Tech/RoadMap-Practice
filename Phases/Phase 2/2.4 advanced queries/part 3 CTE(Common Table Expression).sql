-- WITH average_salary AS (
--     SELECT AVG(salary) AS avg_salary
--     FROM employees
-- )
-- SELECT e.employee_name, e.salary
-- FROM employees as e
-- CROSS JOIN average_salary as a
-- WHERE e.salary > a.avg_salary;


-- Find departments whose average salary is greater than the company-wide average salary.

WITH department_avg AS (
    SELECT
        department_id,
        round(AVG(salary),2) AS avg_salary
    FROM employees
    GROUP BY department_id
),
company_avg AS (
    SELECT round(avg(salary),2) AS avg_salary
    FROM employees
)
SELECT
    d.department_id,
    d.avg_salary
FROM department_avg as d
CROSS JOIN company_avg as c
WHERE d.avg_salary > c.avg_salary;