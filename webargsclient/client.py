import logging
import requests
import urllib.parse

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class Client:

    def __init__(self, url_root):
        print('Client __init__', url_root)
        self.url_root = url_root
        pass

    def create(self, *args, **kwargs):
        print('Client create')
        return self.make_request('POST', *args, **kwargs)
        pass

    def update(self, *args, **kwargs):
        print('Client update')
        return self.make_request('PUT', *args, **kwargs)
        pass

    def get(self, *args, **kwargs):
        print('Client get')
        return self.make_request('GET', *args, **kwargs)
        pass

    def delete(self, *args, **kwargs):
        print('Client delete')
        return self.make_request('DELETE', *args, **kwargs)
        pass

    def make_request(self, method, route='', data=None, params=None, json=None, *args, **kwargs):
        print('Client make_request', method, 'data', data, 'params', params, 'url', self.url_root, args, kwargs)
        if method == 'POST':
            url = urllib.parse.urljoin(self.url_root, route)
            print('Client make_request requests.post', url, data, params)
            r = requests.post(url, data=data, params=params, json=json)
            r.raise_for_status()
            return r
        if method == 'PUT':
            url = urllib.parse.urljoin(self.url_root, route)
            r = requests.put(url, data=data, params=params, json=json)
            r.raise_for_status()
            return r
        if method == 'GET':
            url = urllib.parse.urljoin(self.url_root, route)
            r = requests.get(url, data=data, params=params, json=json)
            r.raise_for_status()
            return r
        if method == 'DELETE':
            url = urllib.parse.urljoin(self.url_root, route)
            r = requests.delete(url, data=data, params=params, json=json)
            r.raise_for_status()
            return r
