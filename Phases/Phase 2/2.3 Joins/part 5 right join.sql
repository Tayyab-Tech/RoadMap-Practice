USE company_employees;
select
	d.department_id,
    d.department_name,
    e.employee_name
from employees as e
right join departments as d
	on e.department_id = d.department_id;