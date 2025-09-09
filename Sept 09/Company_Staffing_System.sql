 CREATE DATABASE IF NOT EXISTS company_db; 
USE company_db; 
 
 DROP TABLE IF EXISTS staff; 
DROP TABLE IF EXISTS departments; 

 CREATE TABLE departments ( 
    dept_id   INT PRIMARY KEY AUTO_INCREMENT, 
    dept_name VARCHAR(50) NOT NULL UNIQUE, 
    location  VARCHAR(50) NOT NULL 
); 

 CREATE TABLE staff ( 
    staff_id    INT PRIMARY KEY AUTO_INCREMENT, 
    first_name  VARCHAR(50) NOT NULL, 
    last_name   VARCHAR(50) NOT NULL, 
    age         INT, 
    salary      DECIMAL(10,2), 
    dept_id     INT NULL, 
    CONSTRAINT fk_staff_dept 
        FOREIGN KEY (dept_id) REFERENCES departments(dept_id) 
); 
 
 INSERT INTO departments (dept_id, dept_name, location) VALUES 
(1, 'IT',         'Bangalore'), 
(2, 'HR',         'Hyderabad'), 
(3, 'Finance',    'Mumbai'),     
(4, 'Marketing',  'Delhi'), 
(5, 'Operations', 'Chennai'), 
(6, 'R&D',        'Pune');       
 INSERT INTO staff (staff_id, first_name, last_name, age, salary, dept_id) VALUES
(101, 'Amit',    'varma',  28, 55000.00, 1), 
(102, 'Sneha',   'Reddy',  32, 60000.00, 2),       
(103, 'Ravi',    'varma', 26, 48000.00, NULL), 
(104, 'Pooja',   'Iyer', 29, 52000.00, 4),  
(105, 'Arjun',   'Mehta', 35, 75000.00, 1),        
(106, 'Divya',   'Nair',  30, 50000.00, 5),       
(107, 'Rahul',   'Kapoor',41, 91000.00, 1),     
(108, 'Priya',   'Singh',  24, 42000.00, NULL), 
(109, 'Vikram',  'Rao', 37, 68000.00, 4),    
(110, 'Neha', 'Kulkarni',  33, 58500.00, 2);    


select * from staff;
select first_name, last_name, salary from staff where salary > 60000;
select * from staff where dept_id is null;
select * from staff order by age asc;
select count(*) from staff;

select * from departments;
select dept_name from departments where location in ('Bangalore','Chennai');
SELECT dept_id, dept_name, location FROM departments WHERE dept_name LIKE 'M%';
SELECT COUNT(DISTINCT location) AS unique_locations FROM departments;
SELECT dept_id, dept_name, location FROM departments ORDER BY dept_name ASC;

select s.first_name,s.last_name,d.dept_name from staff as s 
inner join 
departments as d
on s.dept_id = d.dept_id;
 
select  s.first_name,s.last_name,s.salary from staff as s
inner join
departments as d 
on s.dept_id = d.dept_id where d.dept_name = 'IT';

select s.first_name,s.last_name,d.dept_name from staff as s 
left join 
departments as d
on s.dept_id = d.dept_id;

select s.first_name,s.last_name,s.age,s.salary from staff as s 
left join 
departments as d
on s.dept_id = d.dept_id
where s.dept_id is null;

select  s.first_name,s.last_name,d.dept_name  from staff as s 
right join 
departments as d
on s.dept_id = d.dept_id;

select  d.dept_id,d.dept_name  from staff as s 
right join 
departments as d
on s.dept_id = d.dept_id
where s.dept_id is Null;

SELECT d.dept_id,d.dept_name,d.location,s.staff_id,s.first_name,s.last_name,s.salary
FROM staff s
RIGHT JOIN departments d 
ON s.dept_id = d.dept_id;

