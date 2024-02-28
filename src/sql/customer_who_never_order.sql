-- # Write your MySQL query statement below
SELECT customers.name AS Customers
FROM customers
LEFT JOIN orders
ON customers.id = orders.customerid
WHERE orders.customerid IS NULL;