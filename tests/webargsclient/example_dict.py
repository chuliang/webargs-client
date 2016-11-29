import unittest
from unittest.mock import MagicMock

from webargsclient.client import Client
from webargsclient import decorators
from webargsclient import fields


class Example(Client):

    @decorators.inject_kwargs({
        'title': fields.Str(location='json')
    })
    @decorators.inject_route('/users')
    def create(self, *args, **kwargs):
        print('Example create')
        super().create(*args, **kwargs)

    @decorators.inject_kwargs({
        'id': fields.Str(location='matchdict'),
        'title': fields.Str(location='json')
    })
    @decorators.inject_route('/users/{id}')
    def update(self, *args, **kwargs):
        print('Example update')
        super().update(*args, **kwargs)

    @decorators.inject_kwargs({
        'id': fields.Str(location='matchdict')
    })
    @decorators.inject_route('/users/{id}')
    def get(self, *args, **kwargs):
        print('Example get')
        super().get(*args, **kwargs)

    @decorators.inject_kwargs({
        'id': fields.Str(location='matchdict')
    })
    @decorators.inject_route('/users/{id}')
    def delete(self, *args, **kwargs):
        print('Example delete')
        super().delete(*args, **kwargs)


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Example('http://localhost:8080')

    def tearDown(self):
        pass

    def test_example_create(self):
        self.client.make_request = MagicMock(return_value={})
        self.client.create(title='test')
        self.client.make_request.assert_called_with('POST', route='/users', data=None, params=None, matchdict=None, json={'title': 'test'})

    def test_example_update(self):
        self.client.make_request = MagicMock(return_value={})
        self.client.update(id="test_1", title='test1')
        self.client.make_request.assert_called_with('PUT', route='/users/test_1', data=None, params=None, matchdict={'id': 'test_1'}, json={'title': 'test1'})

    def test_example_get(self):
        self.client.make_request = MagicMock(return_value={})
        self.client.get(id="test_1")
        self.client.make_request.assert_called_with('GET', route='/users/test_1', data=None, params=None, matchdict={'id': 'test_1'}, json=None)

    def test_example_delete(self):
        self.client.make_request = MagicMock(return_value={})
        self.client.delete(id="test_1")
        self.client.make_request.assert_called_with('DELETE', route='/users/test_1', data=None, params=None, matchdict={'id': 'test_1'}, json=None)


if __name__ == '__main__':
    unittest.main()