from marshmallow import Schema
import unittest
from unittest.mock import MagicMock

from webargsclient.client import Client
from webargsclient import decorators
from webargsclient import fields


class CreateSchema(Schema):
    title = fields.Str()


class UpdateSchema(Schema):
    title = fields.Str()
    id = fields.Str(location='matchdict')


class GetSchema(Schema):
    id = fields.Str(location='matchdict')


class DeleteSchema(Schema):
    id = fields.Str(location='matchdict')


class Example(Client):

    @decorators.inject_kwargs(CreateSchema())
    @decorators.inject_route('/users')
    def create(self, *args, **kwargs):
        print('Example create')
        super().create(*args, **kwargs)

    @decorators.inject_kwargs(UpdateSchema())
    @decorators.inject_route('/users/{id}')
    def update(self, *args, **kwargs):
        print('Example update')
        super().update(*args, **kwargs)

    @decorators.inject_kwargs(GetSchema())
    @decorators.inject_route('/users/{id}')
    def get(self, *args, **kwargs):
        print('Example get')
        super().get(*args, **kwargs)

    @decorators.inject_kwargs(DeleteSchema())
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
        self.client.make_request.assert_called_with('POST', route='/users', data=None, params={'title': 'test'}, matchdict=None)

    def test_example_update(self):
        self.client.make_request = MagicMock(return_value={})
        self.client.update(id="test_1", title='test1')
        self.client.make_request.assert_called_with('PUT', route='/users/test_1', data=None, params={'title': 'test1'}, matchdict={'id': 'test_1'})

    def test_example_get(self):
        self.client.make_request = MagicMock(return_value={})
        self.client.get(id="test_1")
        self.client.make_request.assert_called_with('GET', route='/users/test_1', data=None, params=None, matchdict={'id': 'test_1'})

    def test_example_delete(self):
        self.client.make_request = MagicMock(return_value={})
        self.client.delete(id="test_1")
        self.client.make_request.assert_called_with('DELETE', route='/users/test_1', data=None, params=None, matchdict={'id': 'test_1'})


if __name__ == '__main__':
    unittest.main()