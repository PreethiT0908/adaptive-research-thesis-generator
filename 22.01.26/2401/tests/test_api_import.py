import unittest

from fastapi.testclient import TestClient

from app.api import app


class ApiImportTests(unittest.TestCase):
    def test_generate_endpoint_is_available(self):
        client = TestClient(app)
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Adaptive Thesis Generator API Running", response.text)


if __name__ == "__main__":
    unittest.main()
