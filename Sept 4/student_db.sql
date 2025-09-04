create database student_db;
use student_db;
create table students(
id int primary key auto_increment,
age int,
name varchar(100) not null,
course varchar(100)
); 
insert into students(age,name,course)
values
(21,'Rahul Sharma','Data Engineering'),
(22,'Priya','AI Engineer'),
(23,'Aman Kumar','Data Science');

update students
set course='Machine Learning'
where id=2;
delete from students 
where id=3;

SELECT * FROM student_db.students;
