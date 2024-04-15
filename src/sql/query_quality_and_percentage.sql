# Write your MySQL query statement below
-- quality : round(average(rating/position),2)
-- poor_query_percentage: raiting < 3 /total 
-- STEP 1 : GROUP BY QUERY_NAME
-- STEP 2: APPLY QUALITY FORMULA FROM ABOVE
--  STEP 3: make another column to get the count of rating < 3
WITH a AS (
    SELECT query_name , position, rating ,
    CASE
        WHEN rating < 3 THEN 1
        ELSE NULL
    END AS rt
    FROM queries
    WHERE query_name IS NOT NULL
)
SELECT a.query_name , ROUND(AVG(a.rating/a.position),2) AS quality,
ROUND(COUNT(a.rt)*100/COUNT(a.rating),2) AS poor_query_percentage
FROM a
GROUP BY a.query_name;