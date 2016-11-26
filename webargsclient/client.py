import logging


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class Client:

    def __init__(self, url):
        print('Client __init__', url)
        self.url = url
        pass

    def create(self, *args, **kwargs):
        print('Client create')
        self.make_request('POST', *args, **kwargs)
        pass

    def update(self, *args, **kwargs):
        print('Client update')
        self.make_request('PUT', *args, **kwargs)
        pass

    def get(self, *args, **kwargs):
        print('Client get')
        self.make_request('GET', *args, **kwargs)
        pass

    def delete(self, *args, **kwargs):
        print('Client delete')
        self.make_request('DELETE', *args, **kwargs)
        pass

    def make_request(self, method, data=None, params=None):
        print('Client make_request', method, 'data', data, 'params', params, 'url', self.url)
        pass
