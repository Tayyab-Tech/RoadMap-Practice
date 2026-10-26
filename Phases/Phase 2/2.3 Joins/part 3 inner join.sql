select 
	e.employee_id,
    e.employee_name,
    d.department_name
from employees as e
inner join departments as d
	on e.department_id = d.department_id;