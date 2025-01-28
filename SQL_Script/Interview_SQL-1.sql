ALTER TABLE Employee RENAME TO Employee2;
CREATE table Employee (empid int, empname varchar(30), dept varchar(30), sal int)

INSERT INTO employee values(101,'Alice','HR',5000);
INSERT INTO employee values(102,'Bob','Finance',5500);
INSERT INTO employee values(103,'Charlie','IT',6000);
INSERT INTO employee values(104,'David','Marketing',4500);
INSERT INTO employee values(105,'Eva','Sales',7000);
INSERT INTO employee values(106,'Frank','Finance',4800);
INSERT INTO employee values(107,'Grace','IT',5200);
INSERT INTO employee values(108,'Hannah','HR',6500);
INSERT INTO employee values(109,'Ian1','Sales',5400);
INSERT INTO employee values(110,'Jack','Marketing',5900);
INSERT INTO employee values(111,'Alice1','Marketing',5800);
INSERT INTO employee values(112,'Bob1','Sales',6500);
INSERT INTO employee values(113,'Charlie1','Finance',6000);
INSERT INTO employee values(114,'David1','Marketing',4600);
INSERT INTO employee values(115,'Eva1','HR',7100);
INSERT INTO employee values(116,'Frank1','Sales',4800);
INSERT INTO employee values(117,'Grace1','Marketing',5200);
INSERT INTO employee values(118,'Hannah1','Finance',6500);
INSERT INTO employee values(119,'Ian1','IT',5400);
INSERT INTO employee values(120,'Jack1','Marketing',5900);

select * from Employee e where dept = 'Finance'

select * from 
(select dept, sal, DENSE_RANK() over(partition by dept order by sal desc) as ranks
from Employee e )t
where ranks = 1

SELECT 
    dept,
    empid,
    empname,
    sal,
    LEAD(sal) OVER (PARTITION BY dept ORDER BY sal ASC) AS next_salary
FROM 
    employee
where sal > 6000;

SELECT 
    dept,
    empid,
    empname,
    sal,
    LAG(sal) OVER (PARTITION BY dept ORDER BY sal ASC) AS previous_salary
FROM 
    employee
where sal > 6000;


