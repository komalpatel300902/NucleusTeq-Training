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
