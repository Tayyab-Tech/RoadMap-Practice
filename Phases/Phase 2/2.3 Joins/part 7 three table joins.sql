USE company_employees;
select
	e.employee_name,
    d.department_name,
    p.project_name
from employees as e
inner join departments as d
	on e.department_id = d.department_id
inner join employee_projects as ep
	on e.employee_id = ep.employee_id
inner join projects as p
	on ep.project_id = p.project_id;