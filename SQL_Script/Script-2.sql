use dev_db
select * from emp where first_name = 'John'

SELECT last_name,count(*) from emp group by last_name having count(*) > 1
SELECT first_name,count(*) from emp group by first_name having count(*) > 1

create table dept2 as select * from dept where 1 =2

with dept_avg_sal as
(select department_id, avg(salary) as avg_sal
 from emp 
 group by department_id 
),

dept_avg_sal_15k as
(select department_id, avg_sal
 from dept_avg_sal
 where avg_sal < 15000
 )

select * from dept_avg_sal_15k



select first_name, last_name, department_id 
from emp 
where first_name = 'John'
  and last_name = 'Chen'

select first_name, department_id 
from emp 
where department_id in 100


select first_name, last_name, department_id
from emp
where department_id in (select department_id 
                        from emp 
                        where first_name = 'John'
                        and last_name = 'Chen'
                        )
                        

update emp set department_id = 100
where first_name = 'John'
and last_name = 'Chen'



with 
  john_dept as (select department_id,employee_id
                from emp 
                where first_name = 'John'
                and last_name = 'Chen'
                ),
  joh_colleagues as (select first_name, last_name, department_id,employee_id
                   from emp
                   )
select c.first_name, c.last_name ,c.department_id
from joh_colleagues c , john_dept d 
where c.department_id  = d.department_id
  and c.employee_id <> d.employee_id


select employee_id, first_name, last_name, job_id, salary
from emp
order by salary desc
limit 3


select department_id, max(salary) as max_sal
from emp
group by department_id 
order by department_id  

select * from emp

select manager_id, count(employee_id) as cnt_reporter
from emp
group by manager_id

select *
from emp
where manager_id = 102

from emp
group by department_id 


select manager_id, count(employee_id) as cnt_reporter
from emp
group by manager_id


select department_id, count(employee_id) as cnt_emp, min(salary) min_sal, max(salary) as max_sal
from emp
group by department_id 









