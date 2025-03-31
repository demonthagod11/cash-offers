import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestReceiving(unittest.TestCase):
    def test_receive_payment(self):
        response = client.post("/receiving/receive", json={
            "from_account": "123456789",
            "to_account": "987654321",
            "amount": 100.00,
            "currency": "usd",
            "description": "Payment received"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Payment received successfully")

if __name__ == '__main__':
    unittest.main()