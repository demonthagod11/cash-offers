import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestVirtualCard(unittest.TestCase):
    def test_fund_virtual_card(self):
        response = client.post("/virtual_card/fund", json={
            "cardholder_id": "ch_123456789",
            "amount": 100.00
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Virtual card funded successfully")

if __name__ == '__main__':
    unittest.main()