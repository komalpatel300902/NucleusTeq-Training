WITH t AS 
(SELECT customer_number,
COUNT(customer_number) AS cnt
FROM orders GROUP BY customer_number)
SELECT t.customer_number
FROM t
WHERE  t.cnt = ( SELECT MAX(t.cnt) FROM t) ;