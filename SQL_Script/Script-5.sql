
WITH ram_subjects AS (
    SELECT name, subject
    FROM st_subject
    WHERE name = 'RAM'
),
other_students AS (
    SELECT name, subject
    FROM st_subject
    WHERE name <> 'RAM'
),
extra_subjects AS (
    SELECT os.name, os.subject
    FROM other_students os
    WHERE os.subject NOT IN (SELECT subject FROM ram_subjects)
),

extra_counts AS (
    SELECT name, COUNT(*) AS extra_count
    FROM extra_subjects
    GROUP BY name
),

max_extra AS (
    SELECT MAX(extra_count) AS max_count FROM extra_counts
)
SELECT es.name, es.subject
FROM extra_subjects es
JOIN extra_counts ec ON es.name = ec.name
JOIN max_extra m ON ec.extra_count = m.max_count;
