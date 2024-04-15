## SQL

Sql stands for Structured query language. It is used for storing , modefing and maintaining data.

SQL EDITOR : https://www.programiz.com/sql/online-compiler/  

<details >
<summary><b>String Functions</b></summary>

We will be using table `customer` .

Table : `Customer`
|customer_id|	first_name	|last_name|	age|	country|
|-----------|---------------|----------|-----|----|
|1|	John	|Doe	|31	|USA|
|2|	Robert	|Luna	|22	|USA|
|3|	David	|Robinson|	22	|UK|
|4|	John	|Reinhardt|	25	|UK|
|5|	Betty	|Doe	|28	|UAE|

1. CHARINDEX(character, String) : Finds the index of character in String.

Query : `SELECT first_name , CHARINDEX("o",first_name) AS character_index FROM customers;`  
`Output : `

|first_name|	character_index|
|----------|--------------------|
|John	|2|
|Robert	|2|
|David	|0|
|John	|2|
|Betty	|0|

2. CONCAT(string1 , string2,.....) : It concat two String.

Query : `SELECT first_name || " " || last_name AS Full_Name FROM customers;`  

|Full_Name|
|---------|
|John Doe|
|Robert Luna|
|David Robinson|
|John Reinhardt|
|Betty Doe|

3. LENGTH(String) : Return length of String.

Query : `SELECT LENGTH(first_name) AS length_of_name FROM customers;`   
`Output : `  

|length_of_name|
|---------------|
|4|
|6|
|5|
|4|
|5|

4. REPLACE(String, substr_you_want_to_replace, substr) : This function replaces all occurrences of a substring within a string, with a new substring.  

Query : `SELECT REPLACE(first_name, "tt", "rr") AS replaced_string FROM customers;`  
`Output : `

|replaced_string|
|---------------|
|John|
|Robert|
|David|
|John|
|Berry|

5. REVERSE(string) : Reverse the string.  

Query : `SELECT REVERSE(first_name) AS reversed FROM customers;`  
`Output : `
|reversed|
|--------|
|nhoJ|
|treboR|
|divaD|
|nhoJ|
|ytteB|
6. SUBSTRING(string , start , length) : Retrun substring of the strng.

Query : `SELECT SUBSTRING(first_name, 1,3) AS substring FROM customers;`  
`Output : `

|substring|
|---------|
|Joh|
|Rob|
|Dav|
|Joh|
|Bet|

7. LOWER(string) : convert string to lower case.

Query : `SELECT LOWER(first_name) AS lower FROM customers;`  
`Output : `

|lower|
|------|
|john|
|robert|
|david|
|john|
|betty|

8. UPPER(string) : convert string to upper case.

Query : `SELECT UPPER(first_name) AS lower FROM customers;`  
`Output : `

|upper|
|-----|
|JOHN|
|ROBERT|
|DAVID|
|JOHN|
|BETTY|

</details>

<details >
<summary><b>Order by in String</b></summary>

The table names has column name if we use order by in name column :
|name|
|----|
|C_1|
|C_2|
|C_10|
|C_3|
|C_10|
|C_20|
|C_10|

Query : `SELECT name FROM names ORDER BY name;`  
`output :`
|name|
|----|
|C_1|
|C_10|
|C_100|
|C_1000|
|C_2|
|C_20|
|C_3|

</details>
<details>
<summary><b>Joins</b></summary>

customer_id Table
|id	|
|--|
|1|
|2|
|3|
|NULL|
|5|
|1|
|16|
|14|
|12|
|3|

id_list Table
|id|name|
|----|----|	
|1|a|
|2|b|
|3|c|
|5|x|
|2|m|
|6|j|
|1|z|
|NULL|L|

INNER JOIN
Query : `SELECT * FROM customer_id AS c 
INNER JOIN id_list AS i
ON c.id = i.id;
`  
id | id |name|
|--|--|--|
|1 |1 |a|
|1 |1 |z|
|2 |2 |b|
|2 |2 |m|
|3 |3 |c|
|5 |5 |x|
|1 |1 |a|
|1 |1 |z|
|3 |3 |c|

LEFT JOIN
Query : `SELECT * FROM customer_id AS c 
LEFT JOIN id_list AS i
ON c.id = i.id;
` 
|id|id|name|
|--|--|-|
|1 |1 |a|
|1 |1 |a|
|2 |2 |b|
|3 |3 |c|
|3 |3 |c|
|5 |5 |x|
|2 |2 |m|
|1 |1 |z|
|1 |1 |z|
|NULL| NULL |NULL|
|16| NULL |NULL|
|14| NULL |NULL|
|12| NULL |NULL|

RIGHT JOIN
Query : `SELECT * FROM customer_id AS c 
RIGHT JOIN id_list AS i
ON c.id = i.id;
` 
|id|id|name|
|--|--|-|
|1| 1| a|
|1| 1| z|
|2| 2| b|
|2| 2| m|
|3| 3| c|
|5| 5| x|
|1| 1| a|
|1| 1| z|
|3| 3| c|
|NULL| 6 |j|
|NULL| NULL |L|

OUTER JOIN 

Query : `SELECT * FROM   customer_id AS c 
RIGHT JOIN id_list AS i
ON c.id = i.id
UNION
SELECT * FROM customer_id AS c 
LEFT JOIN id_list AS i
ON c.id = i.id;
`
|id|id|name|
|--|--|-|
|1 |1| a|
|1 |1| z|
|2 |2| b|
|2 |2| m|
|3 |3| c|
|5 |5| x|
|NULL| 6 j|
|NULL| NULL| L|
|NULL| NULL| NULL|
|16 |NULL| NULL|
|14 |NULL| NULL|
|12 |NULL| NULL|


Note : `In c.id = i.id Null values will not be compared as it represent absense of value.`
</details>

| Leetcode Question | Answers |
|-------------------|---------|
[Combine Two Tables](https://leetcode.com/problems/combine-two-tables/submissions/1188306822/) | [Solution](src/sql/combine_two_tables.sql)|
|[Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/description/)|[Solution](src/sql/employees_earning_more_than_their_managers.sql)|
|[Duplicate Emails](https://leetcode.com/problems/duplicate-emails/description/)|[Solution](src/sql/dublicate_emails.sql)|
|[Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order/description/)|[Solution](src/sql/customer_who_never_order.sql)|
|[Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/description/)|[Solution]()|
|[Rank Scores](https://leetcode.com/problems/rank-scores/description/)|[Solution](src/sql/rank_score.sql)|
|[Customer Placing the Largest Number of Orders](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/)|[Solution](src/sql/customer_placing_largest_number_of_orders.sql)|
|[Average Time of Process per Machine](https://leetcode.com/problems/average-time-of-process-per-machine/description/?envType=study-plan-v2&envId=top-sql-50)|[Solution](src/sql/average_time_of_process_per_machine.sql)
|[Second Highest Salary](https://leetcode.com/problems/second-highest-salary/description/?lang=pythondata)|[Solution](src/sql/second_highest_salary.sql)|
|[Department Higheat Salary](https://leetcode.com/problems/department-highest-salary/description/?lang=pythondata)|[Solution](src/sql/department_highest_salary.sql)|
|[Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/description/?lang=pythondata)|[Solution](src/sql/department_top_three_salary.sql)|
|[Project Employees I](https://leetcode.com/problems/project-employees-i/description/?envType=study-plan-v2&envId=top-sql-50)|[Solution](src/sql/project_employees_I.sql)|
|[Percentage of Users Attended a Contest](https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/?envType=study-plan-v2&envId=top-sql-50)|[Solution](src/sql/placement_cell.sql)|
|[Queries Quality and Percentage](https://leetcode.com/problems/queries-quality-and-percentage/description/?envType=study-plan-v2&envId=top-sql-50)|[Solution](src/sql/query_quality_and_percentage.sql)|
|[Average Selling Price](https://leetcode.com/problems/average-selling-price/description/?envType=study-plan-v2&envId=top-sql-50)|[Solution](src/sql/average_selling_price.sql)|
|[Biggest Single Number](https://leetcode.com/problems/biggest-single-number/description/?envType=study-plan-v2&envId=top-sql-50)|[Solution](src/sql/biggest_single_number.sql)|
|[The Number of Employees Which Report to Each Employee](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/?envType=study-plan-v2&envId=top-sql-50)|[Solution](src/sql/the_number_of_employee.sql)|
|[Primary Department for Each Employee](https://leetcode.com/problems/primary-department-for-each-employee/description/?envType=study-plan-v2&envId=top-sql-50)|[Solution](src/sql/primary_department_for_each_employee.sql)|
|[Employees Whose Manager Left the Company](https://leetcode.com/problems/employees-whose-manager-left-the-company/description/?envType=study-plan-v2&envId=top-sql-50)|[Solution](src/sql/employee_whose_manager_left_the_company.sql)|
|[Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/description/?envType=study-plan-v2&envId=top-sql-50)|[Solution](src/sql/fix_name_in_table.sql)|
|[Patients With a Condition](https://leetcode.com/problems/patients-with-a-condition/description/?envType=study-plan-v2&envId=top-sql-50)|[Solution](src/sql/patients_with_condition.sql)|
|[List the Products Ordered in a Period](https://leetcode.com/problems/list-the-products-ordered-in-a-period/description/?envType=study-plan-v2&envId=top-sql-50)|[Solution](src/sql/list_of_product_ordered_in_a_period.sql)|

|Hacker Rank |Code|
|------------|---|
|[Binary Tree Nodes](https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true)|[Solution](src/sql/binary_tree_node.sql)|
|[Placements](https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true)|[Solutions](src/sql/placement.sql)|