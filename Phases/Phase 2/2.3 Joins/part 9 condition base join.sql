use company_employees;

select 
	e.employee_name,
    d.department_name,
    e.salary
from employees as e
inner join departments as d
	on e.department_id = d.department_id
where d.department_name = 'IT' and e.salary > 60000
order by e.salary desc;