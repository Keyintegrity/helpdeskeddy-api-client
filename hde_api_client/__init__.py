import base64

import requests


class HelpDeskEddyClient:
    def __init__(self, domain, email, api_key):
        self.domain = domain
        self.email = email
        self.api_key = api_key

    def _get_host(self):
        return 'https://{}/api/v2'.format(self.domain)

    def _get_auth_token(self):
        return base64.b64encode('{}:{}'.format(self.email, self.api_key).encode('utf-8')).decode('utf-8')

    def _get_url(self, path):
        return self._get_host() + path

    def _send_request(self, method, path, **extra_kwargs):
        kwargs = dict(
            method=method,
            url=self._get_url(path),
        )

        if extra_kwargs:
            kwargs.update(extra_kwargs)

        kwargs.setdefault('headers', {})['Authorization'] = 'Basic {}'.format(self._get_auth_token())

        return requests.request(
            **kwargs
        )

    def get(self, path, params=None):
        return self._send_request(method='get', path=path, params=params)

    def post(self, path, json=None):
        return self._send_request(method='post', path=path, json=json)

    def put(self, path, json=None):
        return self._send_request(method='put', path=path, json=json)

    def delete(self, path):
        return self._send_request(method='delete', path=path)
