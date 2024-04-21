from fastapi import FastAPI
from route.route import router
app = FastAPI()

@app.get("/")
async def main():
    return {"msg" : "Hey Everyone"}

app.include_router(router)
