
## Fast API
FastAPI is a high-performance `web framework` for building APIs in Python. It offers rapid development with intuitive APIs and automatic documentation generation. Leveraging `asynchronous programming`, it ensures fast response times even under heavy loads. With built-in data validation, security features, and `WebSocket support`, FastAPI simplifies API development while promoting scalability and reliability.

## Index
1. [**Study-Material**](#study-material)
1. [**FastAPI and MongoDB connection**](#fastapi-and-mongodb-connection)
1. [**CRUD operation Project**](#project-on-fastapi-for-crud-operation)
1. [**Data routing With Jinja Template without BaseModel**](#data-routing-with-jinjatemplate-whithout-basemodel)
1. [**Data routing With Jinja Template with BaseModel**](FAST_API.md/#data-routing-with-jinjatemplate-basemodel-included)
1. [**UnitTesting with FastAPI**](#testing-through-unittest)
1. [**Problem related to HTTP methods**](#problem-related-http-method)
1. [**Connecting Frontend and API using Javascript**](#connecting-frontend-and-api-using-javascript)
1. [**Connecting BaseModel with Javascript**](#connecting-basemodel-with-javascript)


### Study Material 

1. [**YOUTUBE : FastAPI and MongoDB Connection | Channel Name : Eric Roby**](https://youtu.be/QkGqjPFIGCA?si=KU6rj2wynEWrjwg8)   
1. [**YOUTUBE : FastAPI Course | Channel Name : Bitfumes**](https://youtu.be/7t2alSnE2-I?si=XtAPQ1vvthdnoF68)   
1. [**FastAPI VS RouterAPI**](https://youtu.be/D-3JJLpECGQ?si=FZ_YQ07plJFTa4Iu)   
1. [**Testing In FastAPI**](https://fastapi.tiangolo.com/tutorial/testing/)   
1. [**Jinja Documentation**](https://jinja.palletsprojects.com/en/2.11.x/templates/)   
1. [**CRUD Operation using FastAPI**](https://apidog.com/blog/how-to-quickly-implement-crud-operations-with-fastapi/)    
1. [**POST Operation | Jinja x FastAPI**](https://www.fastapitutorial.com/blog/fastapi-jinja-create-job-post/) 
1. [**Create Dynamic WebPage Using FastAPI**](https://www.makeuseof.com/fastapi-jinja-templating-creating-dynamic-web-pages/)    
1. [**Request Class In FastAPI**](https://fastapi.tiangolo.com/advanced/using-request-directly/)
1. [**Use of Form object as Input**](https://github.com/tiangolo/fastapi/discussions/5951)
1. [**Testing for Form(...)**](https://github.com/tiangolo/fastapi/issues/1772)
1. [**FastAPI | TutorialPoint**](https://www.tutorialspoint.com/fastapi/fastapi_accessing_form_data.htm)
1. [**FastAPI Form Data: Handling Form Data Using Pydantic Models**](https://www.getorchestra.io/guides/fastapi-form-data-handling-form-data-using-pydantic-models)
1. [**All abot fetch() Method**](https://www.geeksforgeeks.org/javascript-fetch-method/)


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
### Project On FastAPI for CRUD operation

```File``` : [**Open**](src/api/myfirm/)

```
.
├── myfirm
│   ├── employees.sql
│   ├── requirements.txt
│   ├── main.py
│   ├── test_main.py
│   ├── route
│   │   ├── route.py
│   │   └── __init__.py
│   ├── schema
│   │   ├── schema.py
│   │   └── __init__.py
│   ├── config
│   │   ├── databases.py
│   │   └── __init__.py
│   └── model
        ├── modeles.py
        └── __init__.py
```
```main.py```
```python
# importing the modules
from fastapi import FastAPI
from route.route import router
app = FastAPI()

@app.get("/")
async def main():
    return {"msg" : "Hey Everyone"}

app.include_router(router)

```
```router.py```
```python
# importing the libreries
from fastapi import APIRouter
from config.databases import sql , cursor
from model.models import Register
from schema.schema import list_serial

# creating APIRouter object
router = APIRouter()

@router.post("/")
async def enter_employee_details(info : Register):
    sql_query = f"INSERT INTO employees VALUES ('{info.emp_id}','{info.name}','{info.email}','{info.mobile}','{info.department}');"
    try:
        cursor.execute(sql_query)
    except Exception as e:
        print(e)
    else:
        sql.commit()
        print("Record added successfully !!!")

@router.get("/my_info")
async def my_info():
    result = []
    sql_query = "SELECT * FROM employees;"
    try:
        cursor.execute(sql_query)
    except Exception as e:
        print(e.__context__)
    else:
        values = cursor.fetchall()
        result = list_serial(values)

    return result

@router.put("/{emp_id}")
async def update_name(emp_id : str,name : str):
    sql_query = f"""UPDATE employees 
    SET name = '{name}'
    WHERE emp_id = '{emp_id}';"""
    try:
        cursor.execute(sql_query)
        sql.commit()
    except Exception as e:
        
        print(e)
    else:
        print("Record Updated Successfully !")

@router.delete("/")
async def delete_record(emp_id:str):
    sql_query = f"DELETE FROM employees WHERE emp_id = '{emp_id}';"
    try:
        cursor.execute(sql_query)
        sql.commit()
    except Exception as e:
        print(e)
    else:
        sql.commit()
        print("Record deleted Successfully")


```
```Database Connection : databases.py```
```python
import mysql.connector as sql_connector

try:
    sql = sql_connector.connect(host = "localhost",user = "root", passwd = "", database = "nucleus_teq")
    cursor = sql.cursor()
except Exception as e:
    print(e)
else:
    print("Successfully Connected !!!")
```
```schema.py```
```python
from typing import List

def individual_serial(todo) -> dict:
    dictionary = {
        "emp_id" : todo[0],
        "name" : todo[1],
        "mail_id" : todo[2],
        "mobile_number" : todo[3],
        "department" : todo[4]
    }
    return dictionary

def list_serial(todos) -> List[dict]:
    output = [individual_serial(todo) for todo in todos]
    return output
```
```Testing the Model : test_main.py```
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    print(response.json)

def test_enter_employee_details():
    response = client.post("/",
                           json = {"emp_id": "SQA","name":"lares mortin","email": "kasde@gmail.com","mobile":"6266182634","department":"CSE"})
    assert response.status_code == 200
    print(response.json)

def test_update_name():
    response = client.put("/SQA?name=ljkl")
    assert response.status_code == 200
    print(response.json)

def test_delete():
    response = client.delete("/?emp_id=SQA")
    assert response.status_code == 200

```
### Data Routing with JinjaTemplate whithout BaseModel

**`File`** : [**OPEN**](src/api/registration/)
```
.
├── registration
│   ├── main.py
│   ├── test_main.py
│   ├── templates
│   │   ├── base.html
│   │   ├── blog.html
│   │   ├── footer.html
│   │   └── index.html
│   └── model
        └── modeles.py
        
```
**`JinjaTemplates`**  
JinjaTemplate is a fastapi module used to create frontend template for API's.

**`main.py`**
```python
from fastapi import FastAPI
from model.model import Registration_form ,R

fake_posts_db = [{
    'title': 'First Blog Post',
    'content': 'Content of the first blog post.',
    'author': 'John Doe',
    'publication_date': '2023-06-20',
    'comments': [
        {'author': 'Alice', 'content': 'Great post!'},
        {'author': 'Bob', 'content': 'Intresting read.'}
    ],
    'status': 'published'
},{
    'title': 'Second Blog Post',
    'content': 'Content of the second blog post.',
    'author': 'Jane Smith',
    'publication_date': None,
    'comments': [],
    'status': 'draft'
}]

app = FastAPI()

@app.get("/about")
def about():
    return "All you need to know about Simple Blog"


from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"),name="static")

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def read_posts(request: Request):
    print(request ,"-----")
    print(request.body,"-----")
    return templates.TemplateResponse("blog.html", {"request": request, 
                                                    "posts": fake_posts_db})

@app.get("/login/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})                                                                          

@app.post("/login/", response_class=HTMLResponse)
async def login_details(request: Request):
    a = Registration_form(request)
    await a.load_data()
    print(a.username)
    print(a.password)
    return templates.TemplateResponse("index.html",{"request":request})


```
In above code under `get("/")` header the data is transferd from this application to webpage.

In above code under `get("/login")` and `post("/")` header the data is fetched from webpage to this application.

**`Note`** : In this `BaseModel` from `Pydantic` is not used for post opertation which is crucial for testing purpose.

**`model.py`**
```python
from pydantic import BaseModel, ConfigDict
from fastapi import Request
from typing import Optional, Union

class Registration_form:
    def __init__(self,re: Request):
        self.request = re
        self.username: str = None
        self.password: str = None
    async def load_data(self):
        form = await self.request.form()
        self.username = form.get("username")
        self.password = form.get("password")
```

**`base.html`**

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Simple Blog{% endblock %}</title>
</head>
<body>
    <h1>{% block heading %}Simple Blog{% endblock %}</h1>

    {% block content %}
    {% endblock %}

    {% include "footer.html" %}
</body>
</html>
```
**`blog.html`**
```html
{% extends "base.html" %}

{% block title %}Simple Blog - Blog Page{% endblock %}

{% block heading %}Simple Blog - Blog Page{% endblock %}

{% block content %}
    <h2>Total Number of Posts: {{ posts|length }}</h2>

    {% for post in posts %}
        <div class="post">

            {% if post.status == 'published' %}
                <h3>{{ post.title }}</h3>
                <p>{{ post.content|truncate }}</p>
                <p>Published on: {{ post.publication_date }}</p>

                <h4>Comments:</h4>
                <ul>
                    {% for comment in post.comments %}
                        <li class="comment">{{ comment.author }}-: {{ comment.content }}</li>
                        

                    {% endfor %}
                </ul>
            {% else %}
                <p>This post is still in draft mode.</p>
            {% endif %}
        </div>
        <hr>
    {% endfor %}
{% endblock %}
```
**`footer.html`**
```html
<footer>
    <p>&copy; 2023 Simple Blog. All rights reserved.</p>
    <a href="{{ url_for('about') }}">About</a>
</footer>
```
**`index.html`**
```html
<!DOCTYPE html>
<html lang = "en">
    <head>
        <title>Login Page</title>
    </head>
    <body>
        <form method = "POST">
            <input type = "text" name = "username" placeholder="UserName" value = {{title}}>
            <input type = "text" name = "password" placeholder="UserName" value = {{title}}>
            <button type = "submit" width = "200"></button>
        </form>
    </body>
</html>
```
**`test_main.py`**
```python
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_blog():
    response = client.get("/")
    assert response.status_code == 200
def test_login():
    response = client.post("/login",json= {"username":"komalsdf","password":"sdkfsj"})
    assert response.status_code == 200
```
### Data Routing with JinjaTemplate BaseModel Included
**`Importent Question :`** Why it is important to include the BaseModel from pydantic ?  
**`Answer : `** For testing the model we give input through pydantic architecture only so if BaseModel is not included `we wont be able to do any testing`.

We will use above project for this. Only file which I have `modified` will be shown below rest file will be same.

I will mark modified region with `#modified section start` ... `#modified section end`

**`main.py`**
```python
from fastapi import FastAPI , Form
from model.model import Registration_form ,R

fake_posts_db = [{
    'title': 'First Blog Post',
    'content': 'Content of the first blog post.',
    'author': 'John Doe',
    'publication_date': '2023-06-20',
    'comments': [
        {'author': 'Alice', 'content': 'Great post!'},
        {'author': 'Bob', 'content': 'Intresting read.'}
    ],
    'status': 'published'
},{
    'title': 'Second Blog Post',
    'content': 'Content of the second blog post.',
    'author': 'Jane Smith',
    'publication_date': None,
    'comments': [],
    'status': 'draft'
}]

app = FastAPI()

@app.get("/about")
def about():
    return "All you need to know about Simple Blog"


from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"),name="static")

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
async def read_posts(request: Request):
    print(request ,"-----")
    print(request.body,"-----")
    return templates.TemplateResponse("blog.html", {"request": request, 
                                                    "posts": fake_posts_db})
@app.get("/login/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

#modified section  start                            
async def login_details(f: R,request: Request):

    a = Registration_form(request)
    await a.load_data()
    print(a.username)
    print(a.password)
    print(f.password)
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/login/")
async def l_login_details(request: Request,username = Form(...),password = Form(...) ):
    print(username, password)
    await login_details(R(username=username,password=password),request=request)

#modified section end
```
**`model.py`**
```python
from pydantic import BaseModel, ConfigDict
from fastapi import Request , Form
from typing import Optional, Union

# modified region starts
class R(BaseModel):
    username: str 
    password: str 
# modified region end

class Registration_form:
    def __init__(self,re: Request):
        self.request = re
        self.username: str = None
        self.password: str = None
    async def load_data(self):
        form = await self.request.form()
        self.username = form.get("username")
        self.password = form.get("password")
```
**`test_main.py`**
```python
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_blog():
    response = client.get("/")
    assert response.status_code == 200
def test_login():
    response = client.post("/login",data = {"username":"dsfjhd","password":"sdfdsdfg"})
    assert response.status_code == 200

```
### Testing Through UnitTest
Basic Syntax is given below. This is not my code I have taken it from github.

**`Note`** : Don't run the test file like normal python file it won't work Instead run this coommand `python -m unittest filename` .

```python
from myapp import app

class UploadTest(unittest.TestCase):
    client = TestClient(app)

    def test_upload(self):
        with csv.open("rb") as f:
            filebody = f.read()
        res = self.client.post(
            "/api/upload",
            data={
                "user_id": 1
            },
            files={
                "csv_file": ("filename.csv", filebody),
            },
            headers={"Content-Type": "multipart/form-data"})
        self.assertEqual(status.HTTP_200_OK, res.status_code)
        MyResponseModel.parse_obj(res.json()["data"])
```  
### Problem Related HTTP Method
**`Problem Statement`** : For example we have 4 method `@app.post("/index")`,  <br> `@app.get("/index")`, <br> `@app.put("/index/{empi_id}")`,<br> `@app.delete("/index/{emp_id}")`

How the api will know which method will be called if we click button of `delete` , `update` or `submit`.

We use for this type of binding : 
```HTML
<script>
    function deleteEmployee(empId) {
        if (confirm("Are you sure you want to delete this employee?")) {
            fetch("/delete_emp/"+empId,{method: "DELETE"})
            alert("Employee with ID " + empId + " deleted successfully!");
        }
    }
</script>
```
### Connecting Frontend and API using Javascript

This section holds the solution of above problem that what if the path of `get` `post` `delete` `put` is same.

**`Conclusion`** :  You can have multiple http method having same path but you must specify the method and path fetch method.

**`File`** : [**OPEN**](src/api/api_and_frontend_connection/)
```
.
├── api_and_frontend_connection
│   ├── main.py
│   ├── static
│   ├── templates
│   │   └── index.html      
```

**`main.py`**
```python
from fastapi import FastAPI, HTTPException , Request ,Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
import json
from fastapi.responses import HTMLResponse , JSONResponse
app = FastAPI()

items = [{"id":1,"name":"mango"}]
app.mount("/static", StaticFiles(directory = "static"),name = "static")
templates = Jinja2Templates(directory= "templates")
@app.get("/items/",response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.post("/items/",response_class = HTMLResponse)
async def create_item(request: Request, item_name: str):
    new_item_id = len(items) + 1
    new_item = {"id": new_item_id, "name": item_name}
    items.append(new_item)
    print(items)
    return json.dumps(new_item)

@app.put("/items/{item_id}",response_class = HTMLResponse)
async def update_item(request: Request,item_id: int, item_name: str ):
    for item in items:
        if item["id"] == item_id:
            item["name"] = item_name
            return json.dumps(item)
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}",response_class = HTMLResponse)
async def delete_item(request: Request,item_id: int):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            del items[index]
            return json.dumps({"message": "Item deleted successfully"})
    raise HTTPException(status_code=404, detail="Item not found")

@app.get("/items/{item_id}",response_class = HTMLResponse)
async def read_item(request: Request,item_id: int):
    print(items[item_id])
    return json.dumps(items[item_id])
```

**`index.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI CRUD Example</title>
</head>
<body>
    <h1>FastAPI CRUD Example</h1>

    <h2>Create Item:</h2>
    <input type="text" id="itemNameInput" placeholder="Enter Item Name">
    <button onclick="createItem()">Create Item</button>

    <h2>Update Item:</h2>
    <input type="number" id="updateItemIdInput" placeholder="Enter Item ID">
    <input type="text" id="updateItemNameInput" placeholder="Enter Updated Name">
    <button onclick="updateItem()">Update Item</button>

    <h2>Delete Item:</h2>
    <input type="number" id="deleteItemIdInput" placeholder="Enter Item ID">
    <button onclick="deleteItem()">Delete Item</button>

    <h2>Get Item:</h2>
    <input type="number" id="getItemIdInput" placeholder="Enter Item ID">
    <button onclick="getItem()">Get Item</button>

    <div id="response"></div>

    <script>
        function fetchResponse(response) {
            const responseDiv = document.getElementById('response');
            responseDiv.innerHTML = `<p>${response}</p>`;
        }

        function createItem() {
            const itemName = document.getElementById('itemNameInput').value;
            console.log(itemName);
            fetch('/items/?item_name='+itemName, {method: 'POST'});
        }

        function updateItem() {
            const itemId = document.getElementById('updateItemIdInput').value;
            const itemName = document.getElementById('updateItemNameInput').value;
            fetch(`/items/${itemId}?item_name=${itemName}`, {
                method: 'PUT'
            });
        }
        function deleteItem() {
            const itemId = document.getElementById('deleteItemIdInput').value;
            fetch(`/items/${itemId}`, {
                method: 'DELETE',
            })
            .then(response => response.json())
            .then(data => fetchResponse(JSON.stringify(data)))
            .catch(error => fetchResponse('Error: ' + error.message));
        }

        function getItem() {
            const itemId = document.getElementById('getItemIdInput').value;
            fetch(`/items/${itemId}`,{method:"GET"});
        }
    </script>
</body>
</html>

```
### Connecting BaseModel with Javascript

**`File`** : [**OPEN**](src/api/basemodel_and_javascript_connection//)
```
.
├── basemodel_and_javascript_connection
│   ├── main.py
│   ├── static
│   ├── templates
│   │   └── index.html      
```

**`main.py`**
```python
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import Request
import json
app = FastAPI()

templates = Jinja2Templates(directory= "templates")
app.mount("/static",StaticFiles(directory = "static"),name = "static")


class Item(BaseModel):
    name: str
    description: str

@app.get("/items/",response_class = HTMLResponse)
async def get_index(request : Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/items/",response_class = HTMLResponse)
async def create_item(item: Item):
    print(item.name)
    print(item.description)
    return json.dumps({"name": item.name, "description": item.description})

```
**`index.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Submission</title>
</head>
<body>
    <h2>Submit Form</h2>
    <form id="itemForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Description:</label>
        <input type="text" id="description" name="description"><br><br>
        <button type="submit">Submit</button>
    </form>

    <script>
        document.getElementById("itemForm").addEventListener("submit", async function(event) {
            event.preventDefault();

            const formData = new FormData(this);
            const jsonData = {};
            formData.forEach(function(value, key) {
                jsonData[key] = value;
            });
            const response = await fetch('/items/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(jsonData)
            });

            if (response.ok) {
                const data = await response.json();
                console.log(data);
            } else {
                console.error('Failed to create item');
            }
        });
    </script>
</body>
</html>
```
**`Take Away`**
```javascript
 const response = await fetch('/items/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(jsonData)
            });
```
Here `body: JSON.stringify(jsonData)` will have the data which items which is object of Item(BaseModel) will hold after execution.

#### Q. does `response body` and `HTML body` are same ?
`ChatGPT: `   
No, the "response body" and the HTML <body> tag serve different purposes in web development.

Response Body: In the context of web development and APIs, the "response body" refers to the content of the HTTP response that is sent from the server to the client (e.g., web browser or API consumer). This content can be in various formats, such as JSON, HTML, XML, plain text, etc., depending on the type of response generated by the server.

HTML <body> Tag: In HTML, the <body> tag is used to define the main content of an HTML document. It contains all the content that is visible to the user when they view the web page in a browser. The content within the <body> tag can include text, images, links, videos, forms, and other HTML elements that make up the structure and presentation of the web page.

In summary, while both the response body and the HTML <body> tag deal with content that is displayed to the user, they operate at different levels of web development. The response body is a concept within the HTTP protocol that represents the content of the server's response, while the <body> tag is an HTML element used to structure the visible content of a web page.