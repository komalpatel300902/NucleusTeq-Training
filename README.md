## Introduction

Hello everyone :smile: , this repository holds all my work which I did during the training session provided by **NucleusTeq**. 

## Index
1. **[Introduction](#introduction)**
1. **[Day 1 Git and Github](##Day-1-Git-and-Github)**
1. **[Day 2 Linux](##Day-2-Linux)**
1. **[Day 3 Sql Basics](#day-3-sql-basics)**
## Day 1 Git and Github
### Git
- Git is a version control system that is used to track the changes that we do in a file.
- It is widely used in project where there are multiple user working in a same repository.
### Github
- Github is a website where we store our data (files and folder).
- Github is accessed and utilised through Git tools.

## Day 2 Linux 
- Linux is a open source operating system created by Linus Torvalds. 
#### some Terms in operating System:
1. `kernal` : It is a program which has total control over operating system. In other terms all the process is handled by kernal.
1. `Shell` : It is a user Interface which allows user to interact with the operating system. 

| Linux Practice |
|----------------|
|[Echo statement](src/linux/echo_statement.sh)|
|[variables](src/linux/working_with_variable.sh)|
|[if-else statement](src/linux/if_else_statement.sh)|
|[reading input](src/linux/reading_input.sh)|
|[for-loop](src/linux/for_loop_statement.sh)|
|[for-loop using string](src/linux/for_loop_for_string.sh)|
|[while loop](src/linux/while_loop_statement.sh)|
|[Associated Array](src/linux/assoc_array.sh)|
|[Command Line Argument](src/linux/command_line_argument.sh)|
|[Function with Parameter](src/linux/function_with_parameter.sh)|
|[Indexed Array](src/linux/index_array.sh)|
|[Listing Files](src/linux/listing_files.sh)|
|[Nested While Loop](src/linux/nested_while_loop.sh)|
|[Reading character of String](src/linux/read_each_char_of_input.sh)|
|[Reading Files](src/linux/reading_file.sh)|
|[Square Pattern](src/linux/square_pattern.sh)|

|HACKER RANK | CODE|
|------------|-----|
|[odd natural numbers](https://www.hackerrank.com/challenges/bash-tutorials---looping-and-skipping/problem?isFullScreen=true)|[Solution](src/linux/odd_natural_number.sh)|
|[A Personalized Echo](https://www.hackerrank.com/challenges/bash-tutorials---a-personalized-echo/problem?isFullScreen=true)|[Solution](src/linux/persionalised_echo.sh)|
|[Looping with Numbers](https://www.hackerrank.com/challenges/bash-tutorials---looping-with-numbers/problem?isFullScreen=true)|[Solution](src/linux/looping_with_number.sh)|
|[The World of Numbers](https://www.hackerrank.com/challenges/bash-tutorials---the-world-of-numbers/problem?isFullScreen=true)|[Solution](src/linux/the_world_of_number.sh)|
|[Comparing Numbers](https://www.hackerrank.com/challenges/bash-tutorials---comparing-numbers/problem?isFullScreen=true)|[Solution](src/linux/comparing_number.sh)|
|[Getting started with conditionals](https://www.hackerrank.com/challenges/bash-tutorials---getting-started-with-conditionals/problem?isFullScreen=true)|[Solution](src/linux/getting_started_with_condition.sh)|
|[More on Conditionals](https://www.hackerrank.com/challenges/bash-tutorials---more-on-conditionals/problem?isFullScreen=true)|[Solution](src/linux/more_on_condition.sh)|
|[Middle of a Text File](https://www.hackerrank.com/challenges/text-processing-in-linux---the-middle-of-a-text-file/problem?isFullScreen=true)|[Solution](src/linux/middle_of_a_text_file.sh)|
|[Tail of a Text File #1](https://www.hackerrank.com/challenges/text-processing-tail-1/problem?isFullScreen=true)|[Solution](src/linux/tail_of_a_text_file.sh)|

<details>
<summary>Array</summary>

There are two types of array : 
Associated Array : `declare -A assoc_array`   
- Associate array work with key value pair similar to dictionary in python.   
- Accessing element : `assoc_array[key]`.
- listing keys : `${!acco_array[@]}`

Indexed Array : `declare -a index_array`  
- Index array work with index values similar to list in python.
- Accessing element : `assoc_array[index]`.

Common in both Arrays :  
- Printing all values inside the list : `array_name[@]`
- Length of the list : `${#array_name[@]}`

</details>



## Day 3 Sql Basics
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


|Hacker Rank |Code|
|------------|---|
|[Binary Tree Nodes](https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true)|[Solution](src/sql/binary_tree_node.sql)|
