## Introduction

Hello everyone :smile: , this repository holds all my work which I did during the training session provided by **NucleusTeq**.



<a href = "https://leetcode.com/komal_patel/"><img src ="images/LeetCode.png" width = "42" alt = "LeetCode" style = "border-radius: 50%"> </a>
<a href = "https://www.hackerrank.com/profile/komal14march2002"><img src ="images/Hackerrank.png" width = "42" alt = "LeetCode" style = "border-radius: 50%"> </a>

**Pinned**   
1. [**Greek Gods Assignment**](src/python/pandas_library/greek_gods_exam.ipynb)

1. [**mysql Connection using Python**](PYTHON.md#mysql-connection-using-python)

1. [**MapReduce**](#assignments) **: -> Index->Assignments-> Assignment3 : Map Reduce**

## Index
1. **[Introduction](#introduction)**
1. **[Git and Github](#day-1-git-and-github)**
1. **[Linux](#day-2-linux)**
1. **[Sql Basics](#day-3-sql-basics)**
1. **[Python](#day-4-python)**
1. **[Java](#day-5-java)**
1. **[Docker](#docker)**
1. **[Pandas and SQL](#pandas-and-sql)**
1. **[Assignments](#assignments)**


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

## Day 5 Java

Java is a open source programming language that is used in various fields such as Software development etc ..

|Practice|
|--------|
|[Hello World](src/javafiles/HelloWorld.java)|
|[Creating File](src/javafiles/filehandling/CreateFile.java)|
|[Reading File](src/javafiles/filehandling/ReadingFile.java)|
|[Writing in File](src/javafiles/filehandling/WritingInFile.java)|
[Iterable in Java](src/javafiles/IteratorForClass.java)

For More : [Click Here](JAVA.md)
## Docker
[Documentation Link ](https://docs.docker.com/get-started/02_our_app/)


## Pandas and Sql

|leetcode|SQL | Pandas|
|--------|----|-------|
|[Department Highest Salary](https://leetcode.com/problems/department-highest-salary/description/?lang=pythondata)|[Solution](src/sql/department_highest_salary.sql)|[Solution](src/python/department_highest_salary.py)|
|[Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/description/?lang=pythondata)|[Solution](src/sql/department_top_three_salary.sql)|[Solution](src/python/department_top_three_highest_salary.py)|
|[Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/description/?lang=pythondata)|[Solutions](src/sql/delete_dublicate_emails.sql)  |[Solution](src/python/delete_duplicate_email.py)|
|[Trips and Users](https://leetcode.com/problems/trips-and-users/description/?lang=pythondata)| |[Solutions](src/python/trip_and_users.py)|
|[Consecutive Number](https://leetcode.com/problems/consecutive-numbers/submissions/1214194127/?lang=pythondata)||[Solution](src/python/consicutive_number.py)|
|[Customer Who bought All the Product](https://leetcode.com/problems/customers-who-bought-all-products/submissions/1214236054/?lang=pythondata)||[Solution](src/python/customer_who_bought_all_the_product.py)|
|[Project Employees I](https://leetcode.com/problems/project-employees-i/description/?lang=pythondata)||[Solution](src/python/project_employee_I.py)|
|[Count Salary Categories](https://leetcode.com/problems/count-salary-categories/description/?envType=study-plan-v2&envId=top-sql-50)|[Solution](src/sql/count_salary_categories.sql)||
|[Product Price at a Given Date](https://leetcode.com/problems/product-price-at-a-given-date/description/?envType=study-plan-v2&envId=top-sql-50)||[Solution](src/python/product_price_at_given_data.py)|
|[Sales Person](https://leetcode.com/problems/sales-person/description/?lang=pythondata)||[SOlutions](src/python/sale_person.py)|

## Assignments
<details>
<summary><b>Assignment 1 : Greeks Gods</b></summary>

[**Greeks God Dataset**](src/python/pandas_library/greek_god.csv)    
[**Greeks Goddess Dataset**](src/python/pandas_library/greek_god.csv)

**My Answer** : [Open](src/python/pandas_library/greek_gods_exam.ipynb)
</details>
<details>
<summary><b>Assignment 1</b></summary>
<br>

**Problem Statement** : Your company employs 200 people. They keep records of all the employee information in the *`Employees.csv`* file, which contains the following columns: first name, last name, department, position, and salary. However, they would like to sort the data; first, they would like to group the rows by department lexicographically, and then they would like to sort the rows by salary.
you have been assigned to create a Java application that is capable of carrying out this task.     

**Dataset** : [**open**](src/python/pandas_library/Employees.csv)

</details>

<details>
<summary><b>Assignment 2</b></summary>
<br>

**Problem Statement** : You have a file that stores data about players' scores they achieved in different matches against different teams at different points in time, You have to identify the highest score of each player among all the matches
If the entry is only a string that is the name of the player, and if the entry is pak_55_01_nov that implies the match against Pakistan scored 55 runs on November first.
     

**Dataset** : [**open**](src/python/pandas_library/Scores.csv)

Answer : [**Solution Code**](src/python/pandas_library/assignment_II.ipynb)

</details>
<details>
<summary><b>Assignment 3 : MapReduce</b></summary>

Dataset : [Open](src/python/assignment_dataset.txt)  
Maper File : [Open](src/python/assignment_mapper.py)  
Reduce File : [Open](src/python/assignment_reducer.py)

```bash
komal@komal-VirtualBox:~/NucleusTeq-Training/src/python$ cat assignment_dataset.txt | python3 assignment_mapper.py | sort -k 1,1 | python3 assignment_reducer.py 
```
**OUTPUT**
```
a 3
all 1
All 1
be 2
brown 1
by 1
chuck 2
could 1
cream 1
dog 1
ends 1
for 1
fox 1
How 1
I 1
ice 1
if 1
is 1
jumps 1
lazy 1
much 1
not 1
of 1
or 1
over 1
peck 1
peppers 1
Peter 1
picked 1
pickled 1
Piper 1
question 1
quick 1
scream 3
seashells 1
seashore 1
sells 1
She 1
that 2
the 3
The 1
to 1
To 1
we 1
well 2
wood 2
woodchuck 2
would 1
you 1
```
</details>
