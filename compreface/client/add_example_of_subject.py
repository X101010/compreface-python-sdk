# -*- coding: utf-8 -*-

import os
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

from ..common import ClientRequest


class AddExampleOfSubjectClient(ClientRequest):

    def __init__(self, api_key: str, domain: str, port: str):
        super().__init__()
        self.client_url: str = '/api/v1/faces'
        self.api_key: str = api_key
        self.url: str = domain + ':' + port + self.client_url

    def get(self) -> dict:
        url: str = self.url
        result = requests.get(url, headers={'x-api-key': self.api_key})
        return result.json()

    def post(self, image_path: str = '', subject: str = '') -> dict:
        url: str = self.url + '?subject=' + subject
        name_img: str = os.path.basename(image_path)
        m = MultipartEncoder(
            fields={'file': (name_img, open(image_path, 'rb'))}
        )
        result = requests.post(url, data=m, headers={'Content-Type': m.content_type,
                                                     'x-api-key': self.api_key})
        return result.json()

    def put(self):
        pass

    def delete(self, subject: str = ''):
        url: str = self.url + '?subject=' + subject
        result = requests.delete(url, headers={'x-api-key': self.api_key})
        return result.json()
