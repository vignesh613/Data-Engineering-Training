CREATE DATABASE retailDB;
USE retailDB;

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    brand VARCHAR(50),
    price DECIMAL(10,2),
    stock_quantity INT,
    reorder_level INT,
    supplier_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE stores (
    store_id INT AUTO_INCREMENT PRIMARY KEY,
    store_name VARCHAR(100),
    region VARCHAR(50),
    city VARCHAR(50),
    manager_name VARCHAR(100),
    opening_date DATE,
    contact_number VARCHAR(15)
);

CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(100),
    position VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE,
    store_id INT,
    email VARCHAR(100),
    phone_number VARCHAR(15),
    FOREIGN KEY (store_id) REFERENCES stores(store_id)
);

CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    store_id INT,
    employee_id INT,
    sale_date DATE,
    quantity INT,
    total_amount DECIMAL(10,2),
    payment_method VARCHAR(50),
    discount DECIMAL(5,2),
    customer_name VARCHAR(100),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);


INSERT INTO products (product_name, category, brand, price, stock_quantity, reorder_level, supplier_name)
VALUES
('Laptop', 'Electronics', 'Dell', 55000, 30, 5, 'Tech Supplier Ltd'),
('Headphones', 'Electronics', 'Sony', 2500, 100, 20, 'Sound World'),
('Shirt', 'Clothing', 'Zara', 1500, 50, 10, 'Fashion Hub'),
('Shoes', 'Footwear', 'Nike', 3000, 40, 8, 'SportWear Ltd'),
('Smartphone', 'Electronics', 'Samsung', 35000, 25, 5, 'Mobile Traders'),
('Tablet', 'Electronics', 'Apple', 45000, 15, 3, 'Tech Supplier Ltd'),
('Jacket', 'Clothing', 'Adidas', 4000, 20, 5, 'Fashion Hub'),
('Watch', 'Accessories', 'Fossil', 12000, 35, 7, 'Time Dealers'),
('TV', 'Electronics', 'LG', 65000, 10, 2, 'ElectroMart'),
('Keyboard', 'Electronics', 'Logitech', 1500, 80, 15, 'Tech Supplier Ltd'),
('Mouse', 'Electronics', 'HP', 800, 90, 18, 'Tech Supplier Ltd'),
('Trousers', 'Clothing', 'Levis', 2000, 60, 12, 'Fashion Hub'),
('Sandals', 'Footwear', 'Bata', 1200, 70, 15, 'Footwear Traders'),
('Bag', 'Accessories', 'Wildcraft', 3500, 40, 8, 'Travel Store'),
('Perfume', 'Cosmetics', 'Calvin Klein', 5000, 30, 6, 'Cosmetic World'),
('Sunglasses', 'Accessories', 'RayBan', 8000, 25, 5, 'Vision House'),
('Mixer Grinder', 'Home Appliance', 'Philips', 4500, 20, 5, 'Home Needs'),
('Washing Machine', 'Home Appliance', 'Bosch', 35000, 15, 3, 'Appliance Hub'),
('Refrigerator', 'Home Appliance', 'Whirlpool', 40000, 12, 2, 'Cooling Traders'),
('Earbuds', 'Electronics', 'Boat', 2000, 100, 20, 'Sound World');

INSERT INTO stores (store_name, region, city, manager_name, opening_date, contact_number)
VALUES
('Store A', 'North', 'Delhi', 'Rajesh Mehta', '2015-01-15', '9876543210'),
('Store B', 'South', 'Bangalore', 'Neha Singh', '2016-03-20', '9876500010'),
('Store C', 'East', 'Kolkata', 'Arjun Roy', '2017-07-05', '9876522222'),
('Store D', 'West', 'Mumbai', 'Priya Sharma', '2018-09-12', '9876533333'),
('Store E', 'Central', 'Nagpur', 'Amit Verma', '2020-01-01', '9876544444'),
('Store F', 'North', 'Chandigarh', 'Deepak Joshi', '2021-05-14', '9876555555'),
('Store G', 'South', 'Chennai', 'Kavya Iyer', '2019-02-23', '9876566666'),
('Store H', 'East', 'Patna', 'Ravi Das', '2022-06-18', '9876577777'),
('Store I', 'West', 'Pune', 'Sonal Patel', '2018-04-10', '9876588888'),
('Store J', 'North', 'Lucknow', 'Anjali Gupta', '2023-03-22', '9876599999');


INSERT INTO employees (employee_name, position, salary, hire_date, store_id, email, phone_number)
VALUES
('Rajesh Kumar', 'Sales Associate', 25000, '2020-05-12', 1, 'rajesh@retailltd.com', '9998887771'),
('Neha Sharma', 'Manager', 50000, '2018-03-20', 1, 'neha@retailltd.com', '9998887772'),
('Amit Verma', 'Cashier', 22000, '2021-01-11', 2, 'amit@retailltd.com', '9998887773'),
('Sonal Patel', 'Sales Associate', 24000, '2020-07-01', 2, 'sonal@retailltd.com', '9998887774'),
('Vikram Singh', 'Manager', 52000, '2019-09-13', 3, 'vikram@retailltd.com', '9998887775'),
('Pooja Mehta', 'Sales Associate', 23000, '2021-02-19', 3, 'pooja@retailltd.com', '9998887776'),
('Deepak Joshi', 'Cashier', 21000, '2022-06-05', 4, 'deepak@retailltd.com', '9998887777'),
('Ravi Das', 'Sales Associate', 24000, '2020-10-08', 4, 'ravi@retailltd.com', '9998887778'),
('Anjali Gupta', 'Manager', 51000, '2017-05-30', 5, 'anjali@retailltd.com', '9998887779'),
('Arjun Roy', 'Cashier', 20000, '2022-04-12', 5, 'arjun@retailltd.com', '9998887780'),
('Kavya Iyer', 'Sales Associate', 23000, '2019-11-11', 6, 'kavya@retailltd.com', '9998887781'),
('Suresh Kumar', 'Sales Associate', 24000, '2021-01-02', 6, 'suresh@retailltd.com', '9998887782'),
('Priya Sharma', 'Cashier', 22000, '2020-06-19', 7, 'priya@retailltd.com', '9998887783'),
('Aakash Jain', 'Sales Associate', 23000, '2019-07-24', 7, 'aakash@retailltd.com', '9998887784'),
('Meena Rani', 'Manager', 50000, '2018-02-01', 8, 'meena@retailltd.com', '9998887785'),
('Ramesh Kumar', 'Sales Associate', 25000, '2020-05-21', 8, 'ramesh@retailltd.com', '9998887786'),
('Kiran Desai', 'Cashier', 21000, '2021-09-09', 9, 'kiran@retailltd.com', '9998887787'),
('Sanjay Gupta', 'Sales Associate', 24000, '2020-04-14', 9, 'sanjay@retailltd.com', '9998887788'),
('Manish Yadav', 'Manager', 52000, '2019-12-01', 10, 'manish@retailltd.com', '9998887789'),
('Divya Kapoor', 'Cashier', 20000, '2022-07-15', 10, 'divya@retailltd.com', '9998887790');

INSERT INTO sales (product_id, store_id, employee_id, sale_date, quantity, total_amount, payment_method, discount, customer_name)
VALUES
(1, 1, 1, '2025-09-01', 2, 110000, 'Card', 5, 'Rohit Sharma'),
(2, 1, 2, '2025-09-01', 5, 12500, 'Cash', 0, 'Aditi Mehra'),
(3, 2, 3, '2025-09-02', 3, 4500, 'UPI', 10, 'Sanjay Patel'),
(4, 2, 4, '2025-09-02', 2, 6000, 'Card', 5, 'Nidhi Singh'),
(5, 3, 5, '2025-09-03', 1, 35000, 'Cash', 2, 'Karan Gupta'),
(6, 3, 6, '2025-09-03', 2, 90000, 'Card', 5, 'Simran Kaur'),
(7, 4, 7, '2025-09-04', 3, 12000, 'UPI', 10, 'Ankur Yadav'),
(8, 4, 8, '2025-09-04', 1, 12000, 'Cash', 0, 'Ravi Shukla'),
(9, 5, 9, '2025-09-05', 1, 65000, 'Card', 7, 'Sunita Devi'),
(10, 5, 10, '2025-09-05', 4, 6000, 'UPI', 0, 'Deepa Singh'),
(11, 6, 11, '2025-09-06', 3, 2400, 'Cash', 2, 'Pankaj Tiwari'),
(12, 6, 12, '2025-09-06', 2, 4000, 'Card', 5, 'Rohini Das'),
(13, 7, 13, '2025-09-07', 5, 6000, 'UPI', 10, 'Abhishek Jain'),
(14, 7, 14, '2025-09-07', 3, 10500, 'Cash', 0, 'Ritu Sharma'),
(15, 8, 15, '2025-09-08', 2, 10000, 'Card', 5, 'Ananya Gupta'),
(16, 8, 16, '2025-09-08', 1, 8000, 'UPI', 0, 'Arjun Kapoor'),
(17, 9, 17, '2025-09-09', 2, 9000, 'Cash', 5, 'Shivam Joshi'),
(18, 9, 18, '2025-09-09', 1, 35000, 'Card', 2, 'Priya Rathi'),
(19, 10, 19, '2025-09-10', 1, 40000, 'UPI', 10, 'Nikhil Rao'),
(20, 10, 20, '2025-09-10', 4, 8000, 'Cash', 0, 'Sneha Agarwal');






-- CREATE 
INSERT INTO products (product_name, category, brand, price, stock_quantity, reorder_level, supplier_name)
VALUES ('Gaming Laptop', 'Electronics', 'Asus', 75000, 10, 2, 'Tech Supplier Ltd');

-- READ (all products)
SELECT * FROM products;

-- READ (filter by category)
SELECT * FROM products WHERE category = 'Electronics';

-- UPDATE (change stock after restocking)
UPDATE products 
SET stock_quantity = stock_quantity + 50
WHERE product_id = 1;

-- DELETE (remove discontinued product)
DELETE FROM products WHERE product_id = 20;







-- CREATE
INSERT INTO stores (store_name, region, city, manager_name, opening_date, contact_number)
VALUES ('Store K', 'South', 'Hyderabad', 'Anil Reddy', '2024-01-10', '9876001111');

-- READ
SELECT * FROM stores;

-- READ (filter by region)
SELECT * FROM stores WHERE region = 'North';

-- UPDATE (update manager details)
UPDATE stores
SET manager_name = 'Rahul Khanna', contact_number = '9876002222'
WHERE store_id = 2;

-- DELETE (close a store)
DELETE FROM stores WHERE store_id = 10;





-- CREATE
INSERT INTO employees (employee_name, position, salary, hire_date, store_id, email, phone_number)
VALUES ('Rohit Nair', 'Cashier', 22000, '2023-10-12', 1, 'rohit@retailltd.com', '9998887701');

-- READ (all employees)
SELECT * FROM employees;

-- READ (find employees by store)
SELECT * FROM employees WHERE store_id = 1;

-- UPDATE (promote an employee and raise salary)
UPDATE employees
SET position = 'Senior Sales Associate', salary = salary + 5000
WHERE employee_id = 3;

-- DELETE (remove ex-employee)
DELETE FROM employees WHERE employee_id = 20;





-- CREATE
INSERT INTO sales (product_id, store_id, employee_id, sale_date, quantity, total_amount, payment_method, discount, customer_name)
VALUES (2, 1, 1, '2025-09-12', 3, 7500, 'UPI', 5, 'Rahul Sharma');

-- READ (all sales)
SELECT * FROM sales;

-- READ (sales by date range)
SELECT * FROM sales WHERE sale_date BETWEEN '2025-09-01' AND '2025-09-10';

-- UPDATE (correct a discount entry)
UPDATE sales
SET discount = 10, total_amount = total_amount * 0.9
WHERE sale_id = 5;

-- DELETE (cancel a sale record)
DELETE FROM sales WHERE sale_id = 18;




DELIMITER //
CREATE PROCEDURE GetDailySalesByStore(IN store INT, IN sales_date DATE)
BEGIN
    SELECT st.store_name, SUM(sa.total_amount) AS daily_sales
    FROM sales sa
    JOIN stores st ON sa.store_id = st.store_id
    WHERE sa.store_id = store AND sa.sale_date = sales_date
    GROUP BY st.store_name;
END //
DELIMITER ;

-- 2. Top Selling Products
DELIMITER //
CREATE PROCEDURE GetTopProducts(IN limit_count INT)
BEGIN
    SELECT p.product_name, SUM(sa.quantity) AS total_sold
    FROM sales sa
    JOIN products p ON sa.product_id = p.product_id
    GROUP BY p.product_name
    ORDER BY total_sold DESC
    LIMIT limit_count;
END //
DELIMITER ;

-- 3. Employee Sales Performance
DELIMITER //
CREATE PROCEDURE GetEmployeePerformance(IN emp_id INT)
BEGIN
    SELECT e.employee_name, SUM(sa.total_amount) AS total_sales
    FROM sales sa
    JOIN employees e ON sa.employee_id = e.employee_id
    WHERE e.employee_id = emp_id
    GROUP BY e.employee_name;
END //
DELIMITER ;

-- 4. Region Sales Summary
DELIMITER //
CREATE PROCEDURE GetRegionSales(IN region_name VARCHAR(50))
BEGIN
    SELECT st.region, SUM(sa.total_amount) AS region_sales
    FROM sales sa
    JOIN stores st ON sa.store_id = st.store_id
    WHERE st.region = region_name
    GROUP BY st.region;
END //
DELIMITER ;

-- 5. Stock Alert
DELIMITER //
CREATE PROCEDURE GetLowStock()
BEGIN
    SELECT product_name, stock_quantity, reorder_level
    FROM products
    WHERE stock_quantity < reorder_level;
END //
DELIMITER ;






-- Get daily sales for Store 1 on 1st Sept
CALL GetDailySalesByStore(1, '2025-09-01');

-- Get top 5 products
CALL GetTopProducts(5);

-- Get performance of Employee ID 3
CALL GetEmployeePerformance(3);

-- Get total sales for North region
CALL GetRegionSales('North');

-- Check stock alerts
CALL GetLowStock();





