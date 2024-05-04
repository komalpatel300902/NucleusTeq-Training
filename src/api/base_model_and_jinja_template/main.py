from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from jinja2 import Template
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()
templates = Jinja2Templates(directory = "templates")

# app.mount("/static",StaticFiles(directory = "static"),name= "static")
# Pydantic model for data validation
class Item(BaseModel):
    name: str 
    price: float 
    is_offer: bool 

# Jinja2 template for rendering HTML
template_str = """
<html>
    <head>
        <title>FastAPI with JinjaTemplate</title>
    </head>
    <body>
        <h1>Product Details</h1>
        <p>Name: {{ item.name }}</p>
        <p>Price: {{ item.price }}</p>
        <p>Offer: {% if item.is_offer %}Yes{% else %}No{% endif %}</p>
    </body>
</html>
"""
template = Template(template_str)

@app.get("/items/",response_class=HTMLResponse)
async def input_item(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/items/", response_class=HTMLResponse)
async def create_item(request: Request, name:str = Form(...),price:float = Form(...),is_offer:str = Form(...)):
    # Render HTML template using Jinja2
    print(name)
    print(price)
    print(is_offer)
    item = Item(name=name,price=price,is_offer=is_offer)
    html_content = template.render(item=item)
    return HTMLResponse(content=html_content, status_code=200)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)