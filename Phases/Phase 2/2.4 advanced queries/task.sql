-- Create a complete employee analytical report containing:
-- employee_name
-- department_name
-- salary
-- salary_category
-- project_count
-- workload_category
-- salary_vs_department

-- Where:

-- salary_category
-- High      >= 100000
-- Medium    >= 60000
-- Low       < 60000
-- workload_category
-- Heavy     >= 5 projects
-- Medium    3–4 projects
-- Light     0–2 projects
-- salary_vs_department

-- Compare the employee's salary with their department's average:

-- Above Department Average
-- At Department Average
-- Below Department Average

-- Requirements:

-- At least 2 CTEs
-- JOIN
-- LEFT JOIN
-- GROUP BY
-- COUNT
-- AVG
-- Multiple CASE expressions
-- Meaningful aliases
-- Readable formatting





-- solution : 

use company_employees;
WITH employee_projects_count AS (
    SELECT
        e.employee_id AS employee_id,
        e.employee_name AS employee_name,
        e.salary,
        e.department_id,
        COUNT(ep.project_id) AS project_count
    FROM employees as e
    LEFT JOIN employee_projects ep
        ON e.employee_id = ep.employee_id
    GROUP BY
        e.employee_id,
        e.employee_name,
        e.salary,
        e.department_id
),

department_salary AS (
    SELECT
        department_id,
        AVG(salary) AS department_average_salary
    FROM employees
    GROUP BY department_id
)

SELECT
    epc.employee_name,
    d.department_name AS department_name,
    epc.salary,

    CASE
        WHEN epc.salary >= 100000 THEN 'High'
        WHEN epc.salary >= 60000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category,

    epc.project_count,

    CASE
        WHEN epc.project_count >= 5 THEN 'Heavy'
        WHEN epc.project_count >= 3 THEN 'Medium'
        ELSE 'Light'
    END AS workload_category,

    CASE
        WHEN epc.salary > ds.department_average_salary
            THEN 'Above Department Average'
        WHEN epc.salary = ds.department_average_salary
            THEN 'At Department Average'
        ELSE 'Below Department Average'
    END AS salary_vs_department

FROM employee_projects_count epc

LEFT JOIN departments d
    ON epc.department_id = d.department_id

LEFT JOIN department_salary ds
    ON epc.department_id = ds.department_id

ORDER BY
    d.department_name,
    epc.salary DESC;