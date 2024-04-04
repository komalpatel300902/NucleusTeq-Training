# Write your MySQL query statement below
WITH tbl AS
(
    SELECT account_id as a_id,
    CASE 
        WHEN income < 20000 THEN "Low Salary"
        WHEN income >= 20000 AND income <= 50000 THEN "Average Salary"
        WHEN income > 50000 THEN "High Salary"
    END AS clm
    FROM accounts )
SELECT "Low Salary" AS category , COUNT(tbl.clm) as accounts_count
FROM tbl
WHERE tbl.clm = "Low Salary"
UNION
SELECT "Average Salary" AS category , COUNT(tbl.clm) as accounts_count
FROM tbl
WHERE tbl.clm = "Average Salary"
UNION
SELECT "High Salary" AS category , COUNT(tbl.clm) as accounts_count
FROM tbl
WHERE tbl.clm = "High Salary"
;