__author__ = 'miserylab'

import pytest
from dotenv import load_dotenv
from petstore_tests.test_data.test_data import Users
from petstore_tests.utils.sessions import petstore_api
import json

@pytest.fixture(scope='session', autouse=True)
def env():
    load_dotenv()

@pytest.fixture()
def create_user():
    response = petstore_api().post('/user', data=json.dumps(Users.user_for_test_delete), headers={'Content-Type': 'application/json'})
    assert response.status_code == 200

@pytest.fixture()
def delete_user():

    yield

    username = Users.user_for_test_create['username']
    response = petstore_api().delete(f'/user/{username}')
    assert response.status_code == 200