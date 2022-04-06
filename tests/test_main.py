from fastapi.testclient import TestClient
import json
import os
print(os.getcwd())
from main import app

client = TestClient(app)

with open("headers.json") as headers_json:
    headers = json.load(headers_json)

with open("payload.json") as payload:
    json_payload = json.load(payload)

def test_get_data():
    response = client.get("/data")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_insert_data():
    response = client.post("/insert_data",
                            headers=headers,
                            json=json_payload)
    assert response.status_code == 200
    assert response.json() == {"detail": "Successfull"}