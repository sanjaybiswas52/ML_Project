use dev_db

CREATE TABLE `dept` (
  `department_id` int DEFAULT NULL,
  `department_name` varchar(30) DEFAULT NULL,
  `manager_id` int DEFAULT NULL,
  `location_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `dept1` (
  `employee_id` int DEFAULT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(25) DEFAULT NULL,
  `email` varchar(25) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `hire_date` date DEFAULT NULL,
  `job_id` varchar(10) DEFAULT NULL,
  `salary` float(8,2) DEFAULT NULL,
  `commission_pct` float(2,2) DEFAULT NULL,
  `manager_id` int DEFAULT NULL,
  `department_name` varchar(30) DEFAULT NULL,
  `sn_manager_id` int DEFAULT NULL,
  `regional_location_id` int DEFAULT NULL
  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

create table emp2 as select * from emp where 1=2

select * from emp2

truncate table emp2