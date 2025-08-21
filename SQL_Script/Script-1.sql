use dev_db

select symbol, count(*) 
from (select s.symbol, s.file_date 
from spurt s inner join topgainerlooser gl on (gl.hash_key = s.hash_key)
)t
group by symbol 


select s.symbol, s.file_date , gl.symbol, gl.file_date 
from spurt s inner join topgainerlooser gl on (gl.symbol = s.symbol and gl.file_date = s.file_date)

select s.symbol, s.file_date, s.hash_key , gl.symbol, gl.file_date, gl.hash_key
from spurt s inner join topgainerlooser gl on (gl.symbol = s.symbol and gl.file_date = s.file_date)


select s.symbol, s.file_date from spurt s where file_date  = '10-Mar-2025'

select gl.symbol, gl.file_date from topgainerlooser gl where file_date  = '10-Mar-2025'


create database hive_metadatadb
create database hive_metastore

CREATE USER 'hiveuser'@'%' IDENTIFIED BY 'hive@100';
GRANT ALL PRIVILEGES ON hive_metastore.* TO 'hiveuser'@'%';
FLUSH PRIVILEGES;


use dev_db;

create table sales (OrderID	integer, ord_date date, customer varchar(30), Product varchar(30), Quantity integer, Price float, Total float, Region varchar(30))

select * from sales
select region, max(total) from sales group by region




-- employees definition

CREATE TABLE emp_stage
   ( employee_id int
   , first_name VARCHAR(20)
   , last_name VARCHAR(25)
   , email VARCHAR(25)
   , phone_number VARCHAR(20)
   , hire_date varchar(20) 
   , job_id VARCHAR(10)
   , salary float(8,2)
   , commission_pct float(2,2)
   , manager_id int
   , department_id int
   );
select * from emp
UPDATE emp_stage
SET hire_date = STR_TO_DATE(hire_date, '%d-%b-%Y');

ALTER TABLE emp_stage MODIFY hire_date DATE;
rename table emp_stage to emp
drop table emp

-- departments definition

CREATE TABLE dept
   ( department_id int
   , department_name VARCHAR(30)
   , manager_id int
   , location_id int
   );

select * from dept
select * from emp where employee_id = 200

CREATE TABLE routes(SRL_NO INT, ROUTE_ID INT, ORIGIN VARCHAR(8), DESTINATION VARCHAR(8))

drop table routes

INSERT INTO ROUTES VALUES  (1,201,'DEL','BAN');
INSERT INTO ROUTES VALUES  (2,102,'LUCK','DEL');
INSERT INTO ROUTES VALUES  (3, 123,'RUPC','BRL');
INSERT INTO ROUTES VALUES  (4, 321,'BAN','DEL');
INSERT INTO ROUTES VALUES  (5, 344,'PBT','DEL');
INSERT INTO ROUTES VALUES  (6, 101,'LUCK','BAN');
INSERT INTO ROUTES VALUES  (7, 105,'DEL','LUCK');

SELECT * FROM ROUTES

SELECT 
    LEAST(ORIGIN, DESTINATION) AS origin,
    GREATEST(ORIGIN, DESTINATION) AS destination
FROM routes
GROUP BY 
    LEAST(ORIGIN, DESTINATION),
    GREATEST(ORIGIN, DESTINATION);

SELECT DISTINCT
    LEAST(ORIGIN, DESTINATION) AS origin,
    GREATEST(ORIGIN, DESTINATION) AS destination
FROM routes

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20),
    dob DATE,
    gender ENUM('Male', 'Female'),
    department_id INT,
    admission_year YEAR,
    gpa DECIMAL(3,2)
);




LOAD DATA LOCAL INFILE '/opt/test_data/mysql_datafiles/students_gen.csv'
INTO TABLE students
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

select * from students

--  if required
/* 
 * SHOW VARIABLES LIKE 'local_infile';
 * SET GLOBAL local_infile = 1;
 * SHOW VARIABLES LIKE 'secure_file_priv';

*/
use dev_db
CREATE TABLE dim_employee (
    employee_sk       INT AUTO_INCREMENT PRIMARY KEY,  -- surrogate key
    employee_id       INT NOT NULL,                    -- business/natural key
    first_name        VARCHAR(50),
    last_name         VARCHAR(50),
    department        VARCHAR(100),
    designation       VARCHAR(100),
    manager_id        INT,
    hire_date         DATE,
    birth_date        DATE,
    gender            CHAR(1),
    data_version      varchar(30),
    status            VARCHAR(20),                     -- Active, Inactive, etc.
    start_date        DATE,                            -- for SCD2
    end_date          DATE,                            -- for SCD2
    is_current        BOOLEAN DEFAULT TRUE,            -- for SCD2
    created_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

drop table DEV_DB.dim_employee
CREATE TABLE DEV_DB.dim_employee (
    employee_sk       INT ,  -- surrogate key
    employee_id       INT ,
    first_name        VARCHAR(50),
    last_name         VARCHAR(50),
    department        int,
    designation       VARCHAR(100),
    manager_id        INT,
    hire_date         DATE,
    birth_date        DATE,
    gender            CHAR(1),
    data_version      INT,
    status            INT,                     -- Active, Inactive, etc.
    start_date        DATE,                            -- for SCD2
    end_date          DATE, 
    today             TIMESTAMP,-- for SCD2
    is_current        BOOLEAN DEFAULT TRUE,            -- for SCD2
    created_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at        TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from DEV_DB.dim_employee
delete from DEV_DB.dim_employee where employee_sk = 0

select department_id, count(*) from emp group BY department_id

