INSERT INTO departments
(department_id, department_name)
VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Sales'),
(4, 'Finance');

INSERT INTO employees
(employee_id, employee_name, department_id, manager_id, salary)
VALUES
(101, 'Ali', 1, NULL, 90000),
(102, 'Sara', 1, 101, 70000),
(103, 'Hamza', 2, NULL, 80000),
(104, 'Ayesha', 3, 105, 60000),
(105, 'Bilal', 3, NULL, 100000),
(106, 'Zain', NULL, 101, 50000);

INSERT INTO projects
(project_id, project_name, department_id)
VALUES
(201, 'Website', 1),
(202, 'Recruitment', 2),
(203, 'Marketing', 3);

INSERT INTO employee_projects
(employee_id, project_id)
VALUES
(101, 201),
(102, 201),
(103, 202),
(104, 203),
(105, 203);