import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestPayments(unittest.TestCase):
    def test_send_payment(self):
        response = client.post("/payments/send", json={
            "from_account": "123456789",
            "to_account": "987654321",
            "amount": 100.00,
            "currency": "usd",
            "description": "Payment for services"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Payment sent successfully")

if __name__ == '__main__':
    unittest.main()