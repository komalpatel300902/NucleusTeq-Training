from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_blog():
    response = client.get("/")
    assert response.status_code == 200
def test_login():
    response = client.post("/login",data = {"username":"dsfjhd","password":"sdfdsdfg"})
    assert response.status_code == 200
