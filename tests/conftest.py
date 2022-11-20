import pytest
from dotenv import load_dotenv
from petstore_tests.test_data.test_data import Users
from petstore_tests.utils.sessions import petstore_api
import json
from allure import step

HEADERS = {'Content-Type': 'application/json'}

@pytest.fixture(scope='session', autouse=True)
def env():
    load_dotenv()


@pytest.fixture()
def create_user():
    username = Users.user_for_test_create['username']
    with step(f'get https://petstore.swagger.io/v2/user/{username}'):
        response = petstore_api().get(f'/user/{username}', headers=HEADERS)
    with step('check response stasus code'):
        if response.status_code == 404:
            with step('post https://petstore.swagger.io/v2/user'):
                response = petstore_api().post('/user', data=json.dumps(Users.user_for_test_create),
                                               headers=HEADERS)
            with step('assert status code is 200'):
                assert response.status_code == 200


@pytest.fixture()
def create_user_for_login():
    username = Users.user_login['username']
    with step(f'get https://petstore.swagger.io/v2/user/{username}'):
        response = petstore_api().get(f'/user/{username}', headers=HEADERS)
    with step('check response stasus code'):
        if response.status_code == 404:
            with step('post https://petstore.swagger.io/v2/user'):
                response = petstore_api().post('/user', data=json.dumps(Users.user_login),
                                               headers=HEADERS)
            with step('assert status code is 200'):
                assert response.status_code == 200


@pytest.fixture()
def delete_user():
    yield

    username = Users.user_for_test_create['username']
    with step(f'delete https://petstore.swagger.io/v2/user/{username}'):
        response = petstore_api().delete(f'/user/{username}')
    with step('assert status code is 200'):
        assert response.status_code == 200


@pytest.fixture()
def delete_updated_user():
    yield

    username = Users.user_for_test_update['username']
    with step(f'delete https://petstore.swagger.io/v2/user/{username}'):
        response = petstore_api().delete(f'/user/{username}')
    with step('assert status code is 200'):
        assert response.status_code == 200


@pytest.fixture()
def login():
    username = Users.user_login['username']
    password = Users.user_login['password']
    response = petstore_api().get(f'/user/login?username={username}&password={password}',
                                  headers=HEADERS)
    assert response.status_code == 200


@pytest.fixture()
def logout():
    yield

    response = petstore_api().get('/user/logout', headers=HEADERS)
    assert response.status_code == 200
