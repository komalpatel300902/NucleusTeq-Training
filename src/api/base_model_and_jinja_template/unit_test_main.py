import unittest
from main import app
from fastapi.testclient import TestClient
from fastapi import status
class TestMain(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
    
    def test_get(self):
        res = self.client.get("/items")
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_post(self):
        res = self.client.post("/items",data = {"name":"komal","price":"123.12","is_offer":"True"})
        self.assertEqual(res.status_code, status.HTTP_200_OK)