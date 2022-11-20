import json
from pytest_voluptuous import S
from petstore_tests.schemas.user import user
from petstore_tests.schemas.api_response import api_response
from petstore_tests.test_data.test_data import Users
from petstore_tests.utils.sessions import petstore_api
import allure

HEADERS = {'Content-Type': 'application/json'}


@allure.tag('api', 'positive')
@allure.description('Get user by username')
def test_get_user_by_username(create_user, delete_user):
    username = Users.user_for_test_create['username']

    with allure.step(f'get https://petstore.swagger.io/v2/user/{username}'):
        response = petstore_api().get(f'/user/{username}', headers=HEADERS)

    with allure.step('assert status code is 200'):
        assert response.status_code == 200
    with allure.step('assert schema is valid'):
        assert S(user) == response.json()


@allure.tag('api', 'negative')
@allure.description('Get user by username (User not found)')
def test_get_user_by_username_not_found():
    username = Users.user_not_found['username']

    with allure.step(f'get https://petstore.swagger.io/v2/user/{username}'):
        response = petstore_api().get(f'/user/{username}', headers=HEADERS)

    with allure.step('assert status code is 404'):
        assert response.status_code == 404
    with allure.step('assert message is "User not found"'):
        assert response.json()['message'] == 'User not found'
    with allure.step('assert schema is valid'):
        assert S(api_response) == response.json()


@allure.tag('api', 'positive')
@allure.description('Update user')
def test_update_user(create_user, delete_updated_user):
    username = Users.user_for_test_create['username']
    updated_id = Users.user_for_test_update['id']

    with allure.step(f'put https://petstore.swagger.io/v2/user/{username}'):
        response = petstore_api().put(f'/user/{username}', data=json.dumps(Users.user_for_test_update),
                                      headers=HEADERS)

    with allure.step('assert status code is 200'):
        assert response.status_code == 200
    with allure.step('assert message is id of updated user'):
        assert response.json()['message'] == f'{updated_id}'
    with allure.step('assert schema is valid'):
        assert S(api_response) == response.json()


@allure.tag('api', 'positive')
@allure.description('Create user')
def test_create_user(delete_user):
    id = Users.user_for_test_create['id']

    with allure.step('post https://petstore.swagger.io/v2/user'):
        response = petstore_api().post('/user', data=json.dumps(Users.user_for_test_create),
                                       headers=HEADERS)

    with allure.step('assert status code is 200'):
        assert response.status_code == 200
    with allure.step('assert message is id of created user'):
        assert response.json()['message'] == f'{id}'
    with allure.step('assert schema is valid'):
        assert S(api_response) == response.json()


@allure.tag('api', 'positive')
@allure.description('Delete user')
def test_delete_user(create_user):
    username = Users.user_for_test_create['username']

    with allure.step(f'delete https://petstore.swagger.io/v2/user/{username}'):
        response = petstore_api().delete(f'/user/{username}', headers=HEADERS)

    with allure.step('assert status code is 200'):
        assert response.status_code == 200
    with allure.step('assert message is id of deleted user'):
        assert response.json()['message'] == f'{username}'
    with allure.step('assert schema is valid'):
        assert S(api_response) == response.json()


@allure.tag('api', 'negative')
@allure.description('Test delete user(user not found)')
def test_delete_user_not_found():
    username = Users.user_for_test_create['username']

    with allure.step(f'delete https://petstore.swagger.io/v2/user/{username}'):
        response = petstore_api().delete(f'/user/{username}', headers=HEADERS)

    with allure.step('assert status code is 404'):
        assert response.status_code == 404


@allure.tag('api', 'positive')
@allure.description('Logs user into the system')
def test_login(create_user_for_login, logout):
    username = Users.user_login['username']
    password = Users.user_login['password']

    with allure.step(f'get https://petstore.swagger.io/v2/user/login?username={username}&password={password}'):
        response = petstore_api().get(f'/user/login?username={username}&password={password}',
                                      headers=HEADERS)

    with allure.step('assert status code is 200'):
        assert response.status_code == 200
    with allure.step('assert schema is valid'):
        assert S(api_response) == response.json()


@allure.tag('api', 'positive')
@allure.description('Logs out current logged in user session')
def test_logout(login):
    with allure.step(f'get https://petstore.swagger.io/v2/user/logout'):
        response = petstore_api().get('/user/logout', headers=HEADERS)

    with allure.step('assert status code is 200'):
        assert response.status_code == 200
    with allure.step('assert message is "ok"'):
        assert response.json()['message'] == 'ok'
    with allure.step('assert schema is valid'):
        assert S(api_response) == response.json()
