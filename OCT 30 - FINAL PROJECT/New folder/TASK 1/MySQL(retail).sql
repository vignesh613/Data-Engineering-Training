-- ---------------------------------------------
-- 1. DATABASE AND TABLE CREATION
-- ---------------------------------------------

-- Create the database
CREATE DATABASE IF NOT EXISTS RetailTrackerDB;
USE RetailTrackerDB;

-- 1.1 Products Table
CREATE TABLE IF NOT EXISTS Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    category VARCHAR(100),
    unit_price DECIMAL(10, 2) NOT NULL,
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id) -- Assuming a Suppliers table exists
);

-- 1.2 Inventory Table
CREATE TABLE IF NOT EXISTS Inventory (
    inventory_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    stock_quantity INT NOT NULL,
    reorder_point INT NOT NULL DEFAULT 10, -- Threshold for low-stock
    last_restock_date DATE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- 1.3 Sales Table
CREATE TABLE IF NOT EXISTS Sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT NOT NULL,
    sale_date DATETIME NOT NULL,
    quantity_sold INT NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    region VARCHAR(100),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Create a placeholder Suppliers table for foreign key reference
CREATE TABLE IF NOT EXISTS Suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(255) NOT NULL
);

-- ---------------------------------------------
-- 2. CRUD OPERATIONS (Products & Sales)
-- ---------------------------------------------

-- Sample data for Suppliers
INSERT INTO Suppliers (supplier_id, supplier_name) VALUES (1, 'Tech Distributors'), (2, 'Home Goods Co.');

-- 2.1 CREATE (INSERT) Operations
INSERT INTO Products (product_id, product_name, category, unit_price, supplier_id) 
VALUES 
    (101, 'Wireless Mouse', 'Electronics', 25.00, 1),
    (102, 'Coffee Maker', 'Appliances', 55.00, 2),
    (103, 'USB Cable', 'Electronics', 5.00, 1);

INSERT INTO Inventory (product_id, stock_quantity, reorder_point, last_restock_date)
VALUES 
    (101, 80, 15, '2023-10-01'),
    (102, 12, 10, '2023-09-15'), -- Low stock example
    (103, 5, 50, '2023-10-25'); -- Very low stock example

INSERT INTO Sales (sale_id, product_id, sale_date, quantity_sold, total_amount, region)
VALUES
    (1, 101, NOW(), 2, 50.00, 'West'),
    (2, 102, NOW(), 1, 55.00, 'East'),
    (3, 101, NOW(), 5, 125.00, 'West'),
    (4, 103, NOW(), 1, 5.00, 'North');

-- 2.2 READ (SELECT) Operations
-- Read all products
SELECT * FROM Products; 
-- Read products in a specific category
SELECT product_name, unit_price FROM Products WHERE category = 'Electronics'; 
-- Read Sales data joined with Product name
SELECT s.sale_date, p.product_name, s.quantity_sold, s.total_amount
FROM Sales s
JOIN Products p ON s.product_id = p.product_id;

-- 2.3 UPDATE Operations
-- Update the price of the Wireless Mouse
UPDATE Products
SET unit_price = 28.00
WHERE product_id = 101;
-- Update the stock quantity after a sale (Simulation)
UPDATE Inventory
SET stock_quantity = stock_quantity - 1
WHERE product_id = 102;

-- 2.4 DELETE Operations
-- Delete a product that is no longer carried (use with caution, may require setting ON DELETE CASCADE for foreign keys)
-- DELETE FROM Products WHERE product_id = 103;

-- ---------------------------------------------
-- 3. STORED PROCEDURE: Low-Stock Report
-- ---------------------------------------------

-- Stored procedure to find products where stock_quantity is less than or equal to the reorder_point
DELIMITER $$
CREATE PROCEDURE GetLowStockItems()
BEGIN
    SELECT
        p.product_id,
        p.product_name,
        i.stock_quantity,
        i.reorder_point
    FROM
        Products p
    JOIN
        Inventory i ON p.product_id = i.product_id
    WHERE
        i.stock_quantity <= i.reorder_point
    ORDER BY
        i.stock_quantity ASC;
END$$
DELIMITER ;

-- Execute the stored procedure
CALL GetLowStockItems();