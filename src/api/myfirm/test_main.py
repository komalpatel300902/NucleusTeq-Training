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
