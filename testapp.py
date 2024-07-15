
from fastapi.testclient import TestClient
import app

client = TestClient(app)

def test_read_item_with_nonexistent_id():
    response = client.get("/subfedditid1/?subfedditid=10")
    assert response.status_code == 200
    assert response.json() == {"message": "Output data is empty, use some other filter conditions"}
