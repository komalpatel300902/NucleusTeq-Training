## Python 

Python is a open source , interpreted language that is used in various field such as machine learning , AI and Web.

### Index
1. [Regular Expression](#regexp)
1. [Unit Testing](#unit-testing)
1. [My sql Database Connecton](#mysql-connection-using-python)
1. [Pandas](#pandas)

<details>
<summary>Study Material</summary>

[Set Functions](https://www.geeksforgeeks.org/python-set-methods/?ref=ml_lbp)  
</details>

|Practice|
|--------|
|[Iterators](src/python/iterations_in_python.py)|
|[Class Method](src/python/class_method_in_python.py)|

|Hacker Rank| Code |
|-----------|------|
|[Check Strict Superset](https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true)|[Solution](src/python/check_strict_superset.py)|
|[Triangle Quest](https://www.hackerrank.com/challenges/python-quest-1/problem?isFullScreen=true)|[Solution](src/python/tringle_quest.py)|
|[Mutations](https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true)|[Solution](src/python/mutation.py)|


[Try Except](src/python/try_except_block_no_1.py)  
[Class](src/python/my_class.py)  
[Multiple Inheritance ](src/python/multiple_inheritance.py)  
[Is / == in Python](src/python/is_key_word.py)  
[Method overloading using multipledispatch](src/python/method_overloading_using_multipledispatch.py)  
[Private and Protected Variable](src/python/private_public_variable.py)

## Python Advance

|Exceptions|
|----------|
[ArithmeticError](src/python/exceptionsinpython/arithmetic_exceptions.py)

### REGEXP
[]()
We use ```re``` python library for matching patterns.
```python
import re

txt = "Power of thousand sun"

# findall() function is case sensitive
a1 = re.findall("power",txt)
print(a1)
a2 = re.findall("Power",txt)
print(a2)
```
OUTPUT
```python
[]
['Power']
```
```python
# findall() find pattern in a linear fashion
text = "awawawawawawawawk"
a3 = re.findall("awaw",text)
print(a3)
```
OUTPUT
```python

```
```python
"""Using meta characters"""

script1 = "I watch anime. I have watched Demon Slayer, JJk Spy Family etc ... . anime is fun"
a4 = re.findall("^I",script1)
print(a4)
```
OUTPUT
```python
['I']
```
```python
script2 = "ommmmm ommmmmm ommmmmm oppppppp"
# * checks for 0 or more occurance
a5 = re.findall("om*",script2)
print(a5)

# + checks for 1 or more occurance
a6 = re.findall("om+",script2)
print(a6)

# ? checks for 0 or 1 occurance
a7 = re.findall("om?",script2)
print(a7)
```
OUTPUT
```python
['ommmmm', 'ommmmmm', 'ommmmmm', 'o']
['ommmmm', 'ommmmmm', 'ommmmmm']
['om', 'om', 'om', 'o']
```
```python
# . hold a singe character 
script3 = "a a2 a3 a4 a5 a6"
a8 = re.findall("a.",script3)
print(a8)
```
OUTPUT
```python
['a ', 'a2', 'a3', 'a4', 'a5', 'a6']
```
```python
# $ matches the end of string
script4 = "komal14march2002@gmail.com"
a9 = re.findall("@gmail.com",script4)
print(a9)
```
OUTPUT
```python
['@gmail.com']
```
### Unit Testing

[Calculator File](src/python/unitestinginpython/calculator.py)  
[Unit Testing File](src/python/unitestinginpython/test_calculator.py)

```python
import math
class Calculator:
    """
    This class consist of many functions for numerical operation.

    functions:
        add(int,int)->int
        divide(int,int)->int
        subtract(int,int)->int
        multiply(int,int)->int

    """
   

    def add(self,a: int,b : int) -> int :
        """
        Add function added two number
        
        Args:
            a (int) : first number
            b (int) : second number

        Return:
            int : return sum of a and b
        """
        return a+b
    
    def divide(self , a: int,b: int) -> int:
        """
        divide function divide two number
        
        Args:
            a (int) : first number
            b (int) : second number

        Return:
            int : return quotient of a and b
        """
        return a/b

    def multiply(self, a: int, b: int) -> int:
        """
        multiply function multiply two number
        
        Args:
            a (int) : first number
            b (int) : second number

        Return:
            int : return product of a and b
        """
        return a*b
    
    def subtract(self, a: int,b: int) -> int:
        """
        Subtract function subtract two number
        
        Args:
            a (int) : first number
            b (int) : second number

        Return:
            int : return difference of a and b
        """
        return a-b
```
```python
import unittest
import calculator
class TestClaculator(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This is from setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("This is from setDownClass")

    def setUp(self) -> None:
        print("This is setUp")
        self.c = calculator.Calculator()
    def tearDown(self) -> None:
        print("This is tearDown")

    def test_add(self):
        self.assertEqual(self.c.add(12,23),35)
        self.assertEqual(self.c.add(14,-13),1)
        self.assertEqual(self.c.add(-1,-34),-35)

    def test_subtract(self):
        self.assertEqual(self.c.subtract(12,45),-33)
        self.assertEqual(self.c.subtract(90,-15),105)
        self.assertEqual(self.c.subtract(-12,-45),33)

if __name__ == "__main__":
    unittest.main()
```
OUTPUT
```cmd
This is from setUpClass
This is setUp
This is tearDown
.This is setUp
This is tearDown
.This is from setDownClass

----------------------------------------------------------------------
Ran 2 tests in 0.005s

OK
```
### Mysql connection using Python

[File 1](src/python/mysqlconnectorusingpython/creating_databse.py)

Importing the mysql module
```python
import mysql.connector as mc
```
Building connection to our database
```python
if __name__ == "__main__":
    sql =  mc.connect(host = "localhost" , user = "root" , passwd= "") 
    mycursor = sql.cursor()
```
Creating database
```python
    # Alredy created database nucleus_teq
    mycursor.execute("create database nucleus_teq")
```
Fetching tables of the Database
```python
    mycursor.execute("USE nucleus_teq;")
    mycursor.execute("SHOW TABLES;")
    result = mycursor.fetchall()
    print(result)
```
OUTPUT
```cmd
[('customer_id',), ('customers',), ('demo',), ('emp',), ('group_test',), ('id_list',), ('orders',), ('persons',), ('shopping',), ('table1',), ('table2',), ('table3',)]
```
Creating Table and Inserting values into it.
```python

    mycursor.execute("""CREATE TABLE demo(
                     name varchar(30), 
                     id int);""")
    mycursor.execute("""INSERT INTO demo VALUES
                     ('KOMAL',12),
                     ('nitin',23);""")
    sql.commit()
```
Fetching data from the Table using `fetchone()`
```python
    mycursor.execute("""SELECT * FROM demo;""")
    
    print(mycursor.fetchone())
    print(mycursor.fetchone())
    print(mycursor.fetchone())

```
OUTPUT
```python
('KOMAL', 12)
('nitin', 23)
None
```
Fetching data from the Table using `fetchall()`
```python
    mycursor.execute("""SELECT * FROM demo;""")
    print(mycursor.fetchall())
    print(mycursor.fetchall())
```
OUTPUT
```python
[('KOMAL', 12), ('nitin', 23)]
Traceback (most recent call last):
  File "f:/Git/NucleusTeq Training/src/python/mysqlconnectorusingpython/creating_databse.py", line 29, in <module>
    print(mycursor.fetchall())
  File "D:\Python\lib\site-packages\mysql\connector\cursor.py", line 881, in fetchall
    raise errors.InterfaceError("No result set to fetch from.")
mysql.connector.errors.InterfaceError: No result set to fetch from.
```

Fetching data from the Table using `fetchmany(size)`
```python
    mycursor.execute("""SELECT * FROM demo;""")
    print(mycursor.fetchmany(size = 4))

```
OUTPUT
```python
[('KOMAL', 12), ('nitin', 23)]
```

### Pandas

<details>
<summary>Study material</summary>

[Pandas Cheat Sheet](src/python/pandas_library/Pandas_Cheat_Sheet.pdf)  
[Pandas merge](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.merge.html)

</details>

|Practice|
|--------|
|[Dataframes in Pandas](src/python/pandas_library/data_structure_pandas.ipynb)|
|[concatination in pandas](src/python/pandas_library/concatination_in_pandas.ipynb)|
|[csv file data Extraction](src/python/pandas_library/extraction_from_car_data.ipynb)|
|[Merge in pandas](src/python/pandas_library/mearge_testcase.ipynb)|

|Leetcode|Code|
|--------|----|
|[Combine Two Table](https://leetcode.com/problems/combine-two-tables/submissions/1211055254/?lang=pythondata)|[Solution](src/python/combine_two_tables.py)|
|[Second Highest Salary](https://leetcode.com/problems/second-highest-salary/description/?lang=pythondata)|[Solution](src/python/second_highest_salary.py)|
|[Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/submissions/1211703191/?lang=pythondata)|[Solution](src/python/n_highest_salary.py)|
|[Rank Scores](https://leetcode.com/problems/rank-scores/description/?lang=pythondata)|[Solution](src/python/rank_scores.py)|
|[Department Highest Salary](https://leetcode.com/problems/department-highest-salary/description/?lang=pythondata)|[Solution](src/python/department_highest_salary.py)|
|[Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/description/?lang=pythondata)|[Solution](src/python/department_top_three_highest_salary.py)|
|[Delete Duplicate Emails](https://leetcode.com/problems/delete-duplicate-emails/description/?lang=pythondata)|[Solution](src/python//delete_duplicate_email.py)|