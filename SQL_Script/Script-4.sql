WITH ram_subjects AS (
    SELECT name, sub
    FROM st_subject
    WHERE name = 'RAM'
),
subject_counts AS (
    SELECT name, COUNT(*) AS subject_count
    FROM st_subject
    GROUP BY name
),
ram_count AS (
    SELECT COUNT(*) AS cnt FROM ram_subjects
),
students_with_more_subjects AS (
    SELECT sc.name
    FROM subject_counts sc, ram_count rc
    WHERE sc.subject_count > rc.cnt
)
SELECT yt.name, yt.sub
FROM st_subject yt
JOIN students_with_more_subjects sm
  ON yt.name = sm.name
WHERE yt.sub NOT IN (SELECT sub FROM ram_subjects);


