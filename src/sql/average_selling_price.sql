# Write your MySQL query statement below
-- STEP 1: DAYDIFF(START_DATE , PUSCHASE_DATE)
WITH a AS
(
    SELECT p.product_id AS product_id, ROUND(SUM(p.price*u.units)/SUM(u.units),2) AS average_price
    FROM prices AS p , unitssold AS u
    WHERE (p.product_id = u.product_id) AND (u.purchase_date BETWEEN p.start_date AND p.end_date) 
    GROUP BY p.product_id
),b AS
(
    SELECT DISTINCT(product_id) AS p_id FROM prices
)
SELECT b.p_id AS product_id ,
CASE
    WHEN a.average_price IS NOT NULL THEN a.average_price
    ELSE 0
END AS average_price
FROM b
LEFT JOIN a
ON a.product_id = b.p_id;
