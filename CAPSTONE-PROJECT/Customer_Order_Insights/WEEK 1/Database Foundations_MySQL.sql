-- 1. Database Creation and Selection
CREATE DATABASE IF NOT EXISTS customer_order_insights;
USE customer_order_insights;

-- 2. Table Design: Drop tables if they exist to allow for clean re-creation
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS delivery_status;
DROP TABLE IF EXISTS customers;

-- Table 1: customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_email VARCHAR(100) UNIQUE,
    region VARCHAR(50)
);

-- Table 2: delivery_status (Reference table for status)
CREATE TABLE delivery_status (
    status_id INT PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE
);

-- Insert common delivery statuses
INSERT INTO delivery_status (status_id, status_name) VALUES
(1, 'Pending'),
(2, 'Shipped'),
(3, 'Out for Delivery'),
(4, 'Delivered'),
(5, 'Delayed'); -- This status will be used for the stored procedure

-- Table 3: orders (Includes foreign keys and delay info)
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    expected_delivery_date DATE,
    actual_delivery_date DATE,
    status_id INT NOT NULL,
    delivery_issue VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (status_id) REFERENCES delivery_status(status_id)
);

--------------------------------------------------------------------------------
-- 3. Sample Data Insertion (Needed for CRUD and Stored Procedure to work)

-- Insert sample customer
INSERT INTO customers (customer_id, customer_name, customer_email, region)
VALUES (1, 'Alice Smith', 'alice.s@example.com', 'North');

-- Insert a sample order (CREATE)
INSERT INTO orders (order_id, customer_id, order_date, expected_delivery_date, status_id)
VALUES (101, 1, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 7 DAY), 2); -- Shipped

--------------------------------------------------------------------------------
-- 4. Basic CRUD Operations on orders

-- READ (Fetch the new order)
SELECT * FROM orders WHERE order_id = 101;

-- UPDATE (Change the status of the order to Delayed, status_id = 5)
UPDATE orders
SET status_id = 5, delivery_issue = 'Weather delay'
WHERE order_id = 101;

-- DELETE (Optional: Remove an order)
-- DELETE FROM orders WHERE order_id = 101;

--------------------------------------------------------------------------------
-- 5. Stored Procedure to fetch all delayed deliveries for a customer

DELIMITER $$

CREATE PROCEDURE GetDelayedDeliveries (
    IN p_customer_id INT
)
BEGIN
    -- Fetches orders where the status_name is explicitly 'Delayed'
    SELECT
        o.order_id,
        o.order_date,
        o.expected_delivery_date,
        ds.status_name,
        o.delivery_issue
    FROM
        orders o
    JOIN
        delivery_status ds ON o.status_id = ds.status_id
    WHERE
        o.customer_id = p_customer_id
        AND ds.status_name = 'Delayed';
END$$

DELIMITER ;

-- Example Execution of the Stored Procedure
CALL GetDelayedDeliveries(1);