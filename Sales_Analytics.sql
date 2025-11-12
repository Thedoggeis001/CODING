-- Sales_Analytics.sql
-- Simulated database for sales tracking and reporting

CREATE DATABASE SalesDB;
USE SalesDB;

-- 1. Create tables
CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE Sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    quantity INT,
    sale_date DATE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- 2. Insert sample data
INSERT INTO Products (product_name, price)
VALUES ('Laptop', 1200.00), ('Mouse', 25.00), ('Keyboard', 45.00), ('Monitor', 250.00);

INSERT INTO Sales (product_id, quantity, sale_date)
VALUES
(1, 2, '2024-01-10'),
(2, 5, '2024-01-11'),
(3, 3, '2024-01-12'),
(1, 1, '2024-02-01'),
(4, 2, '2024-02-10');

-- 3. Calculate total revenue per product
SELECT p.product_name,
       SUM(s.quantity * p.price) AS total_revenue
FROM Sales s
JOIN Products p ON s.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC;

-- 4. Monthly sales performance
SELECT DATE_FORMAT(s.sale_date, '%Y-%m') AS month,
       SUM(s.quantity * p.price) AS monthly_revenue
FROM Sales s
JOIN Products p ON s.product_id = p.product_id
GROUP BY month
ORDER BY month;
