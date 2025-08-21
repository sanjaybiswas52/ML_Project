select * from students

SELECT subject, student_id, marks, DENSE_RANK() OVER (PARTITION BY subject order by marks desc) as rank FROM students s                

SELECT 
    subject, 
    student_id, 
    marks
FROM (
    SELECT 
        subject, 
        student_id, 
        marks, 
        DENSE_RANK() OVER (PARTITION BY subject ORDER BY marks DESC) AS rank
    FROM students
) ranked_students
WHERE rank = 2;



SELECT 
    dept,
    empid,
    empname,
    sal,
    LEAD(sal) OVER (PARTITION BY dept ORDER BY sal ASC) AS next_salary
FROM 
    employee
where sal > 6000;

select * from employee where dept in ('Finance','Sales')

create table route (rn integer, depa)

select * from Employee2 e 
select * from Employees

CREATE TABLE sqlite.emp (empid int, empname varchar(30), dept int, sal int);

insert into emp(empid,empname,sal) values (select empid, empname, sal from Employee  )
select * from departments 
