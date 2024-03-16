# Write your MySQL query statement below
WITH tbl1 AS 
(SELECT *
FROM activity
WHERE activity_type = "end"),tbl2 AS 
(SELECT *
FROM activity
WHERE activity_type = "start")
SELECT tbl1.machine_id,
ROUND((SUM(tbl1.timestamp)- SUM(tbl2.timestamp))/COUNT(tbl1.process_id),3) AS processing_time
FROM tbl1
INNER JOIN tbl2
ON tbl1.machine_id = tbl2.machine_id AND tbl1.process_id = tbl2.process_id
GROUP BY tbl1.machine_id;