-- Create a report showing each employee's name, manager's name, department, and project. 
-- Include employees even if they have no manager, department, or project.
-- Expected columns: employee_name, manager_name, department_name, project_name

-- Requirements:
-- Use employees as the main table.
-- Use a SELF JOIN for the manager.
-- Join departments.
-- Join employee_projects.
-- Join projects.
-- Preserve all employees.
-- Use meaningful aliases.
-- Sort by employee name

use company_employees;

select 
	e.employee_name as employee_name,
    m.employee_name as manager_name,
    d.department_name,
    p.project_name
from employees as e

left join employees as m
	on e.employee_id = m.employee_id

left join departments as d
	on e.department_id = d.department_id

left join employee_projects as ep
	on e.employee_id = ep.employee_id

left join projects as p
	on ep.project_id = p.project_id
    
order by employee_name;