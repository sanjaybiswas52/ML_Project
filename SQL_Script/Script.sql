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





a	1	46
b	2	50
c	3	76