# test_app.py
import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        eval.testing = True
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

if __name__ == '__main__':
    unittest.main()
