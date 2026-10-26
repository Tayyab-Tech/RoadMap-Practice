CREATE DATABASE IF NOT EXISTS company_employees;
USE company_employees;

create table departments(
	department_id INT primary key,
    department_name varchar(50)
);

create table employees (
	employee_id int primary key,
    employee_name varchar(100),
    department_id int,
    manager_id int,
    salary decimal(10,2),
    foreign key (department_id)
		references departments(department_id)
);

create table projects(
	project_id int primary key,
    project_name varchar(100),
    department_id int,
    foreign key (department_id) 
		references departments(department_id)
);

create table employee_projects (
	employee_id int,
    project_id int,
    primary key (employee_id,project_id),
    foreign key (employee_id) 
		references employees(employee_id),
	foreign key (project_id) 
		references projects(project_id)
);