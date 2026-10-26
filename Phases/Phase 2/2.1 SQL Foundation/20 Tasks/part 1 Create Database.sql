create database IF not exists employeedata;
use employeedata;
CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(150) NOT NULL,
    salary DECIMAL(10,2) CHECK (salary >= 10000),
    age INT CHECK (age >= 18),
    city VARCHAR(200) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE employee AUTO_INCREMENT = 100;