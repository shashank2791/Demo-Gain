show databases;
create table department (
  dept_no int primary key, 
  dept_name text,
  dept_location text
);


create table  employee(
  emp_no int primary key,
  emp_name text,
  emp_age smallint check (emp_age >= 18),
  emp_gender char check (emp_gender in ('M', 'F','m','f')),
  dept_no int,
  foreign key (dept_no )  references department(dept_no) on delete cascade
);

show tables;

desc department;
desc employee;


create table courses(
course_id int, 
course_name text,
course_faculty text,
course_duration text, 
course_price int
);

show tables;
desc courses;


create table course_copy as select * from courses;

show tables;

desc course_copy;

alter table course_copy add column course_location text;
alter table course_copy add column course_size smallint;

desc course_copy;

alter table course_copy drop column  course_price;
alter table course_copy drop column course_faculty;

desc course_copy;

alter table course_copy rename column course_size to batch_size;

desc course_copy;
