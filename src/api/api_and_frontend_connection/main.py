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