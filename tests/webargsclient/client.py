import unittest

from webargsclient.client import Client


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client('http://localhost:8080')

    def tearDown(self):
        pass

    def test_client(self):
        pass


if __name__ == '__main__':
    unittest.main()
