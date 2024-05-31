from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException

app = FastAPI()

@app.get("/{variable}")
def index(variable: int):
    if variable > 5:
        raise HTTPException(status_code = 400 , detail="Value is greater than 5")
    return {"message": "the value is less than and equal to 5"}
        