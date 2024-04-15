-- # Write your MySQL query statement below
SELECT user_id , CONCAT_WS("",UPPER(SUBSTR(name,1,1)), LOWER(SUBSTR(name,2,100))) AS name
FROM users
ORDER BY user_id;