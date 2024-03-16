## Introduction

Hello everyone :smile: , this repository holds all my work which I did during the training session provided by **NucleusTeq**. 

## Index
1. **[Introduction](#introduction)**
1. **[Day 1 Git and Github](#day-1-git-and-github)**
1. **[Day 2 Linux](#day-2-linux)**
1. **[Day 3 Sql Basics](#day-3-sql-basics)**
1. **[Day 4 Python](#day-4-python)**
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

For more : [Click Here](LINUX.md)


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

For more : [Click Here](SQL.md)

## Day 4 Python 

Python is a open source , interpreted language that is used in various field such as machine learning , AI and Web.

|Hacker Rank| Code |
|-----------|------|
|[Check Strict Superset](https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true)|[Solution](src/python/check_strict_superset.py)|

For More : [Click Here](PYTHON.md)