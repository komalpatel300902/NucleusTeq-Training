from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from route.route import router


class Profile(BaseModel):
    username:str
    id:str
    name: str
    revenue: Optional[int]


app = FastAPI()
app.include_router(router)

            
@app.get("/")
def root_file():
    return {"Message" : "Hello Everyone"}

@app.get("/about")
def about():
    return {"Owner":"Komal Patel",
            "Date": "18-04-2024"}

@app.post("/simple_profile")
def simple_profile():
    return {"Message": "Hello Everyone"}

@app.post("/profile")
def profile(profile: Profile):
    with open(r"database.txt","a") as file:
        lst = list(map(str,[profile.username,profile.id,profile.name,profile.revenue,"\n"]))
        file.writelines(lst)
    return {"profile": profile}

@app.get("/display_data")
def display_data(id:int):
    with open("database.txt","r") as file:
        a = file.read(100)
    return {"koaml":"message"}

