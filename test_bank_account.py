import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestBankAccount(unittest.TestCase):
    def test_add_bank_account(self):
        response = client.post("/bank_account/add", json={
            "account_number": "123456789",
            "routing_number": "987654321",
            "account_type": "checking"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Bank account added successfully")

if __name__ == '__main__':
    unittest.main()