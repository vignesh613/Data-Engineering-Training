
-- ===============================
-- Week 1 - MySQL Script
-- ===============================

CREATE DATABASE IF NOT EXISTS customer_order_tracker;
USE customer_order_tracker;

-- Customers Table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    postal_code VARCHAR(10),
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Orders Table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    product_name VARCHAR(100),
    quantity INT,
    amount DECIMAL(10,2),
    payment_mode VARCHAR(20),
    status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Delivery Status Table
CREATE TABLE IF NOT EXISTS delivery_status (
    delivery_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    courier_name VARCHAR(50),
    tracking_number VARCHAR(50),
    delivery_date DATE,
    estimated_date DATE,
    delivery_status VARCHAR(20),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Insert Customers
INSERT INTO customers (first_name, last_name, email, phone, city, state, country, postal_code) VALUES
('Arjun', 'Mehta', 'arjun@example.com', '9876543210', 'Bangalore', 'Karnataka', 'India', '560001'),
('Neha', 'Kapoor', 'neha@example.com', '9876543211', 'Delhi', 'Delhi', 'India', '110001'),
('Ramesh', 'Patil', 'ramesh@example.com', '9876543212', 'Mumbai', 'Maharashtra', 'India', '400001'),
('Priya', 'Sharma', 'priya@example.com', '9876543213', 'Jaipur', 'Rajasthan', 'India', '302001'),
('Vikas', 'Nair', 'vikas@example.com', '9876543214', 'Kochi', 'Kerala', 'India', '682001'),
('Sneha', 'Rao', 'sneha@example.com', '9876543215', 'Hyderabad', 'Telangana', 'India', '500001'),
('Anil', 'Singh', 'anil@example.com', '9876543216', 'Lucknow', 'UP', 'India', '226001'),
('Kiran', 'Das', 'kiran@example.com', '9876543217', 'Kolkata', 'WB', 'India', '700001'),
('Meena', 'Joshi', 'meena@example.com', '9876543218', 'Chennai', 'TN', 'India', '600001'),
('Rajesh', 'Iyer', 'rajesh@example.com', '9876543219', 'Pune', 'Maharashtra', 'India', '411001'),
('Divya', 'Reddy', 'divya@example.com', '9876543220', 'Vizag', 'AP', 'India', '530001'),
('Sameer', 'Gupta', 'sameer@example.com', '9876543221', 'Indore', 'MP', 'India', '452001'),
('Manoj', 'Pillai', 'manoj@example.com', '9876543222', 'Trivandrum', 'Kerala', 'India', '695001'),
('Aarti', 'Chopra', 'aarti@example.com', '9876543223', 'Nagpur', 'Maharashtra', 'India', '440001'),
('Farhan', 'Ali', 'farhan@example.com', '9876543224', 'Ahmedabad', 'Gujarat', 'India', '380001'),
('Sunita', 'Verma', 'sunita@example.com', '9876543225', 'Kanpur', 'UP', 'India', '208001'),
('Ajay', 'Bose', 'ajay@example.com', '9876543226', 'Patna', 'Bihar', 'India', '800001'),
('Rekha', 'Menon', 'rekha@example.com', '9876543227', 'Coimbatore', 'TN', 'India', '641001'),
('Deepak', 'Kulkarni', 'deepak@example.com', '9876543228', 'Goa', 'Goa', 'India', '403001'),
('Pooja', 'Thakur', 'pooja@example.com', '9876543229', 'Bhopal', 'MP', 'India', '462001');

-- Insert Orders
INSERT INTO orders (customer_id, order_date, product_name, quantity, amount, payment_mode, status) VALUES
(1, '2025-09-01', 'Laptop', 1, 60000.00, 'Card', 'Processing'),
(2, '2025-09-02', 'Mobile Phone', 2, 45000.00, 'UPI', 'Shipped'),
(3, '2025-09-03', 'Headphones', 1, 2000.00, 'Cash', 'Delivered'),
(4, '2025-09-04', 'Smart Watch', 1, 7000.00, 'NetBanking', 'Delayed'),
(5, '2025-09-05', 'Tablet', 1, 15000.00, 'Card', 'Processing'),
(6, '2025-09-06', 'Shoes', 2, 4000.00, 'Cash', 'Cancelled'),
(7, '2025-09-07', 'Refrigerator', 1, 30000.00, 'Card', 'Shipped'),
(8, '2025-09-08', 'Microwave', 1, 12000.00, 'UPI', 'Delivered'),
(9, '2025-09-09', 'AC', 1, 35000.00, 'Card', 'Processing'),
(10, '2025-09-10', 'Washing Machine', 1, 25000.00, 'Cash', 'Delivered'),
(11, '2025-09-11', 'Books', 5, 1500.00, 'UPI', 'Processing'),
(12, '2025-09-12', 'TV', 1, 40000.00, 'Card', 'Shipped'),
(13, '2025-09-13', 'Shoes', 1, 2500.00, 'Cash', 'Delivered'),
(14, '2025-09-14', 'Bag', 2, 3000.00, 'UPI', 'Delayed'),
(15, '2025-09-15', 'Camera', 1, 55000.00, 'Card', 'Processing'),
(16, '2025-09-16', 'Printer', 1, 8000.00, 'NetBanking', 'Cancelled'),
(17, '2025-09-17', 'Keyboard', 1, 1200.00, 'Cash', 'Delivered'),
(18, '2025-09-18', 'Monitor', 1, 10000.00, 'Card', 'Shipped'),
(19, '2025-09-19', 'Power Bank', 2, 3000.00, 'UPI', 'Delivered'),
(20, '2025-09-20', 'Router', 1, 2500.00, 'Card', 'Processing');

-- Insert Delivery Status
INSERT INTO delivery_status (order_id, courier_name, tracking_number, delivery_date, estimated_date, delivery_status) VALUES
(1, 'BlueDart', 'TRK001', NULL, '2025-09-07', 'Pending'),
(2, 'DTDC', 'TRK002', '2025-09-06', '2025-09-05', 'Delivered'),
(3, 'FedEx', 'TRK003', '2025-09-04', '2025-09-04', 'Delivered'),
(4, 'EcomExpress', 'TRK004', NULL, '2025-09-07', 'Delayed'),
(5, 'BlueDart', 'TRK005', NULL, '2025-09-08', 'Pending'),
(6, 'DTDC', 'TRK006', NULL, '2025-09-09', 'Cancelled'),
(7, 'FedEx', 'TRK007', '2025-09-10', '2025-09-10', 'Delivered'),
(8, 'EcomExpress', 'TRK008', '2025-09-09', '2025-09-09', 'Delivered'),
(9, 'BlueDart', 'TRK009', NULL, '2025-09-12', 'Pending'),
(10, 'DTDC', 'TRK010', '2025-09-11', '2025-09-11', 'Delivered'),
(11, 'FedEx', 'TRK011', NULL, '2025-09-14', 'Pending'),
(12, 'EcomExpress', 'TRK012', NULL, '2025-09-15', 'Shipped'),
(13, 'BlueDart', 'TRK013', '2025-09-15', '2025-09-15', 'Delivered'),
(14, 'DTDC', 'TRK014', NULL, '2025-09-16', 'Delayed'),
(15, 'FedEx', 'TRK015', NULL, '2025-09-18', 'Pending'),
(16, 'EcomExpress', 'TRK016', NULL, '2025-09-20', 'Cancelled'),
(17, 'BlueDart', 'TRK017', '2025-09-19', '2025-09-19', 'Delivered'),
(18, 'DTDC', 'TRK018', NULL, '2025-09-21', 'Shipped'),
(19, 'FedEx', 'TRK019', '2025-09-21', '2025-09-21', 'Delivered'),
(20, 'EcomExpress', 'TRK020', NULL, '2025-09-23', 'Pending');


-- 1. Read all customers
SELECT * FROM customers;

-- 2. Read all orders with customer details
SELECT o.order_id, c.first_name, c.last_name, o.product_name, o.quantity, o.amount, o.status
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;

-- 3. Read delayed deliveries
SELECT o.order_id, o.product_name, d.delivery_status, d.estimated_date
FROM orders o
JOIN delivery_status d ON o.order_id = d.order_id
WHERE d.delivery_status = 'Delayed';

-- 4. Read total spent by each customer
SELECT c.customer_id, c.first_name, c.last_name, SUM(o.amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_spent DESC;

-- =========================
-- UPDATE (Modify Records)
-- =========================

-- 1. Update order status
UPDATE orders
SET status = 'Delivered'
WHERE order_id = 1;

-- 2. Update customer phone number
UPDATE customers
SET phone = '9998887776'
WHERE customer_id = 5;

-- 3. Update delivery status for delayed order
UPDATE delivery_status
SET delivery_status = 'Delivered', delivery_date = CURDATE()
WHERE order_id = 4;

-- 4. Increase amount by 10% for a specific customer’s orders
UPDATE orders
SET amount = amount * 1.10
WHERE customer_id = 2;

-- =========================
-- DELETE (Remove Records)
-- =========================

-- 1. Delete an order
DELETE FROM delivery_status
WHERE order_id = 20;

DELETE FROM orders
WHERE order_id = 20;

-- 2. Delete delivery record for a cancelled order
DELETE FROM delivery_status
WHERE delivery_status = 'Cancelled';

-- 3. Delete a customer and cascade orders (if ON DELETE CASCADE was enabled)
DELETE FROM customers
WHERE customer_id = 20;

-- 4. Delete orders older than a specific date
DELETE FROM orders
WHERE order_date < '2025-09-05';

-- Stored Procedures
DELIMITER $$

CREATE PROCEDURE GetDelayedDeliveries(IN cust_id INT)
BEGIN
    SELECT o.order_id, o.product_name, d.delivery_status, d.estimated_date
    FROM orders o
    JOIN delivery_status d ON o.order_id = d.order_id
    WHERE o.customer_id = cust_id
      AND d.delivery_status = 'Delayed';
END $$

CREATE PROCEDURE GetTotalSpent(IN cust_id INT)
BEGIN
    SELECT c.first_name, c.last_name, SUM(o.amount) AS total_spent
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    WHERE c.customer_id = cust_id
    GROUP BY c.first_name, c.last_name;
END $$

CREATE PROCEDURE GetOrdersByPayment(IN mode VARCHAR(20))
BEGIN
    SELECT * FROM orders WHERE payment_mode = mode;
END $$

CREATE PROCEDURE GetOrderCountByStatus()
BEGIN
    SELECT status, COUNT(*) AS total_orders
    FROM orders
    GROUP BY status;
END $$

CREATE PROCEDURE GetCustomerOrders(IN cust_id INT)
BEGIN
    SELECT o.order_id, o.product_name, o.quantity, o.amount, o.status, o.order_date
    FROM orders o
    WHERE o.customer_id = cust_id
    ORDER BY o.order_date DESC;
END $$

DELIMITER ;

