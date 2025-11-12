-- Employee_Management.sql
-- Creates a simple company database with employees and departments

CREATE DATABASE CompanyDB;
USE CompanyDB;

-- 1. Create tables
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL
);

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hire_date DATE,
    salary DECIMAL(10,2),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

-- 2. Insert sample data
INSERT INTO Departments (dept_name)
VALUES ('IT'), ('HR'), ('Finance');

INSERT INTO Employees (first_name, last_name, hire_date, salary, dept_id)
VALUES
('Alice', 'Smith', '2020-05-10', 4200.00, 1),
('Bob', 'Jones', '2018-11-01', 3900.00, 2),
('Carla', 'Rossi', '2019-06-15', 5200.00, 1),
('David', 'Brown', '2021-02-20', 3100.00, 3);

-- 3. Useful queries
SELECT e.first_name, e.last_name, d.dept_name, e.salary
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id
ORDER BY d.dept_name;

-- 4. Find the average salary per department
SELECT d.dept_name, AVG(e.salary) AS avg_salary
FROM Employees e
JOIN Departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_name;
