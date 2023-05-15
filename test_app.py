# test_app.py
import unittest
from eval import eval

class AppTestCase(unittest.TestCase):
    def setUp(self):
        eval.testing = True
        self.eval = eval.test_client()

    def test_hello_world(self):
        response = self.eval.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

if __name__ == '__main__':
    unittest.main()
