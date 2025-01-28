
SELECT * FROM lt_shoppers
SELECT * FROM lt_orders

select * from Employees e 
select * from departments d 

SELECT DATE_FORMAT(date,'%d.%m.%Y')) FROM lt_orders

SELECT * FROM lt_products

SELECT count(*) FROM (
SELECT shopper_id 
FROM lt_shoppers 
UNION
SELECT shopper_id
FROM lt_orders 
)test


SELECT *
FROM lt_shoppers 
ORDER BY income DESC LIMIT 2

create table salary(Employee_id integer, sal float, deptno integer)
INSERT ALL
   INTO employees (employee_id, sal, deptno) VALUES (101, 5000, 10)
   INTO departments (department_id, department_name) VALUES (1, 'HR')
   INTO employees (employee_id, name, department_id) VALUES (102, 'Bob', 2)
   INTO departments (department_id, department_name) VALUES (2, 'Finance')
SELECT * FROM dual;
   