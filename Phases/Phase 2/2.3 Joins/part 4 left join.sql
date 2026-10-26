USE company_employees;
-- select
-- 	e.employee_id,
--     e.employee_name,
--     d.department_name
-- from employees as e
-- left join departments as d
-- 	on e.department_id = d.department_id;


SELECT
    d.department_id,
    d.department_name,
    e.employee_name
FROM departments AS d
LEFT JOIN employees AS e
    ON d.department_id = e.department_id;