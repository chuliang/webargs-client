from marshmallow import Schema
import unittest

from webargsclient.client import Client
from webargsclient import decorators
from webargsclient import fields


class CompanyCreate(Schema):
    commercial_name = fields.String(required=True,
                                    load_from='commercialName',
                                    location='json',
                                    dump_to='commercialName')

    class Meta:
        strict = True


class Example(Client):

    @decorators.inject_kwargs(CompanyCreate())
    @decorators.inject_route('/v2/companies')
    def create(self, *args, **kwargs):
        print('Example create')
        super().create(*args, **kwargs)


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Example('http://localhost:6547')

    def tearDown(self):
        pass

    def test_example_create(self):
        self.client.create(commercial_name='test')


if __name__ == '__main__':
    unittest.main()
