import unittest

from webargsclient import decorators


class TestClient(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_inject_kwargs(self):
        @decorators.inject_kwargs({})
        def test(self, params, data, matchdict):
            return self, params, data, matchdict
        _self, _params, _data, _matchdict = test(None)
        self.assertIsNone(_self)
        self.assertIsNone(_params)
        self.assertIsNone(_data)
        self.assertIsNone(_matchdict)


if __name__ == '__main__':
    unittest.main()
