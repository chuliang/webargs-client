import unittest

from webargsclient import decorators


class TestClient(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_inject_kwargs(self):
        @decorators.inject_kwargs({})
        def test(self, params, data):
            return self, params, data
        _self, _params, _data = test(None)
        self.assertIsNone(_self)
        self.assertIsNone(_params)
        self.assertIsNone(_data)


if __name__ == '__main__':
    unittest.main()
