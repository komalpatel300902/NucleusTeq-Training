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
1. **[Fast Api](#fast-api)**
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

## 1. Creating Image Using Dockerfile

[MY APP](src/docker/myapp/)

#### Dockerfile
``` docker
FROM python:latest
WORKDIR /app
COPY . .
EXPOSE 3000
CMD ["python","main.py"]
```
#### bash $

```bash
root@komal-VirtualBox:/home/komal/NucleusTeq-Training/src/docker/myapp# docker build -t myapp:01 
. 
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  3.072kB
Step 1/5 : FROM python:latest
:
:
Successfully built fa9120a7be03
Successfully tagged myapp:01

```
```bash
root@komal-VirtualBox:/home/komal/NucleusTeq-Training/src/docker/myapp# docker images
REPOSITORY                TAG       IMAGE ID       CREATED          SIZE
myapp                     01        fa9120a7be03   12 seconds ago   1.02GB
third-demo                latest    24cdb97230c3   32 hours ago     1.02GB
second-demo               latest    62350c0fe3eb   33 hours ago     1.02GB
```
#### Running the Image
```bash
root@komal-VirtualBox:/home/komal/NucleusTeq-Training/src/docker/myapp# docker run myapp:01
Hello everyone !!!
```
#### Running Image in interactive Terminal Mode
```bash
root@komal-VirtualBox:/home/komal/NucleusTeq-Training/src/docker/myapp# docker run -it myapp:01 bash
root@c588b3ef8955:/app# 
```
#### Files inside the Container
```bash
root@c588b3ef8955:/app# ls
Dockerfile  main.py
root@c588b3ef8955:/app# cd ..
root@c588b3ef8955:/# ls
app  boot  etc   lib    media  opt   root  sbin  sys  usr
bin  dev   home  lib64  mnt    proc  run   srv   tmp  var
root@c588b3ef8955:/# 
```
#### Seeing the Status of the Container
```bash
CONTAINER ID   IMAGE      COMMAND   CREATED         STATUS         PORTS      NAMES
c588b3ef8955   myapp:01   "bash"    2 minutes ago   Up 2 minutes   3000/tcp   nervous_kare
```
#### Stoping the Container
```bash
root@komal-VirtualBox:/home/komal/NucleusTeq-Training# docker stop nervous_kare
nervous_kare
root@komal-VirtualBox:/home/komal/NucleusTeq-Training# 
```
#### Pushing Image to Docker hub
[**My Docker Hub**](https://hub.docker.com/repository/docker/komal300902/myapp/)
```bash
root@komal-VirtualBox:/home/komal/NucleusTeq-Training# docker tag myapp:01 komal300902/myapp:01
```
```bash
root@komal-VirtualBox:/home/komal/NucleusTeq-Training# docker push komal300902/myapp:01
```


## Fast API
### Study Material 

[YOUTUBE : FastAPI and MongoDB Connection | Channel Name : Eric Roby ](https://youtu.be/QkGqjPFIGCA?si=KU6rj2wynEWrjwg8)  
[YOUTUBE : FastAPI Course | Channel Name : Bitfumes ](https://youtu.be/7t2alSnE2-I?si=XtAPQ1vvthdnoF68)   
[FastAPI VS RouterAPI ](https://youtu.be/D-3JJLpECGQ?si=FZ_YQ07plJFTa4Iu)


#### FastAPI and MongoDB Connection 

```python
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://root:root@mycluster.jtujc9h.mongodb.net/?retryWrites=true&w=majority&appName=MyCluster"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

```
```bash
WARNING:  StatReload detected changes in 'main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [13590]
Pinged your deployment. You successfully connected to MongoDB!
INFO:     Started server process [13646]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

```


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
