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
    id = fields.Str()


class GetSchema(Schema):
    id = fields.Str()


class DeleteSchema(Schema):
    id = fields.Str()


class Example(Client):

    @decorators.inject_kwargs(CreateSchema())
    def create(self, *args, **kwargs):
        print('Example create')
        super().create(*args, **kwargs)

    @decorators.inject_kwargs(UpdateSchema())
    def update(self, *args, **kwargs):
        print('Example update')
        super().update(*args, **kwargs)

    @decorators.inject_kwargs(GetSchema())
    def get(self, *args, **kwargs):
        print('Example get')
        super().get(*args, **kwargs)

    @decorators.inject_kwargs(DeleteSchema())
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
        self.client.make_request.assert_called_with('POST', data=None, params={'title': 'test'})

    def test_example_update(self):
        self.client.make_request = MagicMock(return_value={})
        self.client.update(id="test_1", title='test1')
        self.client.make_request.assert_called_with('PUT', data=None, params={'title': 'test1', 'id': 'test_1'})

    def test_example_get(self):
        self.client.make_request = MagicMock(return_value={})
        self.client.get(id="test_1")
        self.client.make_request.assert_called_with('GET', data=None, params={'id': 'test_1'})

    def test_example_delete(self):
        self.client.make_request = MagicMock(return_value={})
        self.client.delete(id="test_1")
        self.client.make_request.assert_called_with('DELETE', data=None, params={'id': 'test_1'})


if __name__ == '__main__':
    unittest.main()