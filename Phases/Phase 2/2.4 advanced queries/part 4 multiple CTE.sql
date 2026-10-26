WITH
department_avg AS (
    SELECT
        department_id,
        AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
),

high_salary_departments AS (
    SELECT department_id
    FROM department_avg
    WHERE avg_salary > 70000
)

SELECT
    e.employee_name,
    e.salary,
    e.department_id
FROM employees e
WHERE e.department_id IN (
    SELECT department_id
    FROM high_salary_departments
);