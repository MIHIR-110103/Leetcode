# Write your MySQL query statement below
SELECT DISTINCT
    a.machine_id , ROUND(AVG(e.timestamp - a.timestamp),3) as processing_time
FROM
    Activity a
INNER JOIN 
    Activity e
ON 
    a.machine_id = e.machine_id AND a.process_id = e.process_id
WHERE
    a.activity_type = "start" AND e.activity_type = "end"
GROUP BY
    a.machine_id

