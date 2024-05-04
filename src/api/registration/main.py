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