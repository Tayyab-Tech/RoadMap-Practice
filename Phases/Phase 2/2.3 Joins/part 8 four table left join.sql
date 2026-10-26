USE company_employees;
SELECT
    e.employee_id,
    e.employee_name,
    d.department_name,
    p.project_name
FROM employees AS e
LEFT JOIN departments AS d
    ON e.department_id = d.department_id
LEFT JOIN employee_projects AS ep
    ON e.employee_id = ep.employee_id
LEFT JOIN projects AS p
    ON ep.project_id = p.project_id;