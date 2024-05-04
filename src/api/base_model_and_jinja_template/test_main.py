
from main import app
from fastapi import status
from fastapi.testclient import TestClient

client = TestClient(app)
def test_get():
    res = client.get("/items")
    assert res.status_code == status.HTTP_200_OK

def test_post():
    res = client.post("/items",data = {"name":"komal","price":"123.23","is_offer":"True"})
    assert res.status_code == status.HTTP_200_OK
