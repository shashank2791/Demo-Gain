create table Department (
    deptno int, 
    dept_name text, 
    dept_manager text,
    address_id int
);

create table Address(
    address_id int, 
    city text, 
    state text
);


create table employee(
    emp_no int, 
    emp_name text,
    emp_sal decimal, 
    deptno int
);


select e.emp_no, e.emp_name, e.emp_sal, e.dept_no, d.dept_name, d.dept_manager, a.city, a.state from employee e inner join Department d on 
e.deptno = d.deptno inner join Address a on d.address_id = a.address_id;



create table bankaccount(
    acc_no int primary key, 
    acc_opened_date date, 
    status text, 
    balance decimal
);

create table transaction(
    acc_no int,
    trans_type char, 
    trans_date date, 
    trans_amount decimal,
    foreign key (acc_no) references bankaccount (acc_no) on delete cascade
);



create table employee(
    emp_no int, 
    emp_name text,
    emp_sal decimal, 
    department text,
    manager_name text
);

insert into employee values (1, "a", 100, "asd", "fjty");
insert into employee values (2, "b", 200, "absd", "fwj");
insert into employee values (3, "c", 300, "agsd", "fttj");
insert into employee values (4, "d", 400, "aesd", "fbbj");
insert into employee values (5, "e", 500, "ashd", "fssj");
insert into employee values (6, "f", 600, "asyd", "ferrj");




select department group by department join select sum(emp_sal) as dept_sal from employee group by department;

select emp_sal < (select emp_sal < (select emp_sal < (select emp_sal from employee order by desc)));


























