__author__ = 'miserylab'

import json

import pytest
from pytest_voluptuous import S
from petstore_tests.schemas.users import user
from petstore_tests.test_data.test_data import Users
from petstore_tests.utils.sessions import petstore_api
import allure
from allure import step


@pytest.mark.positive
@allure.tag('api')
@allure.story('User')
@allure.title('Test create user')
def test_create_user(delete_user):
    with step('post https://petstore.swagger.io/v2/user'):
        response = petstore_api().post('/user', data=json.dumps(Users.user_for_test_create), headers={'Content-Type': 'application/json'})
    with step('assert status code is 200'):
        assert response.status_code == 200


@pytest.mark.positive
@allure.tag('api')
@allure.story('User')
@allure.title('Test delete user')
def test_delete_user(create_user):

    username = Users.user_for_test_create['username']
    with step(f'delete https://petstore.swagger.io/v2/user/{username}'):
        response = petstore_api().delete(f'/user/{username}')
    with step('assert status code is 200'):
        assert response.status_code == 200


@pytest.mark.negative
@allure.tag('api')
@allure.story('User')
@allure.title('Test delete user(user not found)')
def test_delete_user_not_found():
    username = Users.user_for_test_create['username']
    with step(f'delete https://petstore.swagger.io/v2/user/{username}'):
        response = petstore_api().delete(f'/user/{username}', headers={'Content-Type': 'application/json'})
    with step('assert status code is 404'):
        assert response.status_code == 404


@pytest.mark.positive
@allure.tag('api')
@allure.story('User')
@allure.title('Test update user')
def test_update_user(create_user, delete_updated_user):
    username = Users.user_for_test_create['username']
    with step(f'put https://petstore.swagger.io/v2/user/{username}'):
        response = petstore_api().put(f'/user/{username}', data=json.dumps(Users.user_for_test_update), headers={'Content-Type': 'application/json'})
    with step('assert status code is 200'):
        assert response.status_code == 200


@pytest.mark.skip(reason="Expected:404, Actual:200")
@pytest.mark.negative
@allure.tag('api')
@allure.story('User')
@allure.title('Test update user(User not found)')
def test_update_user_not_found():
    username = Users.user_not_found['username']
    with step(f'put https://petstore.swagger.io/v2/user/{username}'):
        response = petstore_api().put(f'/user/{username}', data=json.dumps(Users.user_for_test_update), headers={'Content-Type': 'application/json'})
    with step('assert status code is 404'):
        assert response.status_code == 404



@pytest.mark.positive
@allure.tag('api')
@allure.story('User')
@allure.title('Test login (positive))')
def test_login_positive(create_user_for_login, logout):
    username = Users.user_login['username']
    password = Users.user_login['password']
    with step(f'get https://petstore.swagger.io/v2/user/login?username={username}&password={password}'):
        response = petstore_api().get(f'/user/login?username={username}&password={password}', headers={'Content-Type': 'application/json'})
    with step('assert status code is 200'):
        assert response.status_code == 200


@pytest.mark.skip(reason="при вводе несуществующих username/password приходит 200, а не 400")
@pytest.mark.negative
@allure.tag('api')
@allure.story('User')
@allure.title('Test login (negative)')
def test_login_negative():
    username = Users.user_not_found['username']
    password = Users.user_not_found['password']
    with step(f'get https://petstore.swagger.io/v2/user/login?username={username}&password={password}'):
        response = petstore_api().get(f'/user/login?username={username}&password={password}', headers={'Content-Type': 'application/json'})
    with step('assert status code is 400'):
        assert response.status_code == 400

@pytest.mark.positive
@allure.tag('api')
@allure.story('User')
@allure.title('Test logout')
def test_logout(login):
    response = petstore_api().get('/user/logout', headers={'Content-Type': 'application/json'})
    assert response.status_code == 200


# @pytest.mark.positive
# @allure.tag('api')
# @allure.story('User')
# @allure.title('Test User Schema')
# def test_user_schema():
#     username = Users.user_for_test_create['username']
#     response = petstore_api().get(f'/user/{username}', headers={'Content-Type': 'application/json'})
#     print(response.json())
#     assert S(user) == response.json()