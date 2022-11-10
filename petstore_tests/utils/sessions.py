__author__ = 'miserylab'

import os
from petstore_tests.utils.requests_helper import BaseSession


def petstore_api() -> BaseSession:
    api_url = os.getenv('petstore_api_url')
    return BaseSession(base_url=api_url)