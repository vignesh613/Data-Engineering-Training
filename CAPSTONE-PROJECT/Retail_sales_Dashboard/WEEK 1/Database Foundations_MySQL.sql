-- PERFECTED WEEK 1 CAPSTONE SQL SCRIPT
-- Executes all required tasks without producing foreign key errors (Error Code: 1451).

-- 1. DATABASE SETUP & SCHEMA
--------------------------------------------------------------------------------
CREATE DATABASE RetailSalesDB;
USE RetailSalesDB;

CREATE TABLE Stores (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100) NOT NULL,
    region VARCHAR(50) NOT NULL
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    store_id INT,
    FOREIGN KEY (store_id) REFERENCES Stores(store_id)
);

CREATE TABLE Sales (
    sale_id INT PRIMARY KEY,
    store_id INT,
    product_id INT,
    sale_date DATE NOT NULL,
    quantity INT NOT NULL,
    revenue DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (store_id) REFERENCES Stores(store_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- 2. INDEXING
--------------------------------------------------------------------------------
CREATE INDEX idx_sales_product ON Sales(product_id);
CREATE INDEX idx_stores_region ON Stores(region);

-- 3. CRUD OPERATIONS
--------------------------------------------------------------------------------

-- CREATE (Insert data)
INSERT INTO Stores (store_id, store_name, region) VALUES (101, 'Downtown Flagship', 'North');
INSERT INTO Products (product_id, product_name, category, price) VALUES 
(1, 'Laptop Pro', 'Electronics', 1200.00),
(2, 'Eco Mug', 'Home Goods', 15.50);

INSERT INTO Sales (sale_id, store_id, product_id, sale_date, quantity, revenue) VALUES
(10001, 101, 1, '2024-10-01', 5, 6000.00),
(10002, 101, 2, '2024-10-01', 50, 775.00);

-- READ (Select data)
SELECT * FROM Sales WHERE store_id = 101 AND sale_date = '2024-10-01';

-- UPDATE (Change data)
UPDATE Sales SET quantity = 6, revenue = 7200.00 WHERE sale_id = 10001;

-- DELETE (Error-free removal of Product ID 2)
DELETE FROM Sales WHERE product_id = 2; -- Must delete dependent child records first
DELETE FROM Products WHERE product_id = 2; -- Now safely delete the parent record

-- 4. STORED PROCEDURE
--------------------------------------------------------------------------------
DELIMITER $$
CREATE PROCEDURE CalculateDailySales(
    IN target_store_id INT, 
    IN target_date DATE
)
BEGIN
    SELECT
        S.store_id,
        S.sale_date,
        SUM(S.revenue) AS TotalDailyRevenue
    FROM Sales S
    WHERE S.store_id = target_store_id AND S.sale_date = target_date
    GROUP BY S.store_id, S.sale_date;
END$$
DELIMITER ;

-- Example of Stored Procedure Execution
-- CALL CalculateDailySales(101, '2024-10-01');