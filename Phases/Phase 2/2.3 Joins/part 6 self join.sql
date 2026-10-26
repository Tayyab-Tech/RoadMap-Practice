USE company_employees;
select 
	e.employee_name as employee,
    m.employee_name as manager
from employees as e
left join employees as m
	on e.manager_id = m.manager_id;