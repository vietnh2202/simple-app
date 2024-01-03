import unittest
from app import app

class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello DevOps Team!')

    def test_liveness(self):
        response = self.app.get('/healthz/liveness')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'OK')

    def test_readiness(self):
        response = self.app.get('/healthz/readiness')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'OK')

if __name__ == '__main__':
    unittest.main()