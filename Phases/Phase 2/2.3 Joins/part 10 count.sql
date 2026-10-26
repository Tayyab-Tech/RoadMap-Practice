select 
	d.department_name,
    count(e.employee_id) as employee_count
from departments as d
left join employees as e
	on d.department_id = e.department_id
group by 
	d.department_id,
    d.department_name
order by employee_count desc;