__author__ = 'miserylab'

import json

import pytest
# from pytest_voluptuous import S
# from petstore_tests.schemas.users import user
from petstore_tests.test_data.test_data import Users
from petstore_tests.utils.sessions import petstore_api
import allure


@pytest.mark.positive
@allure.tag('api')
@allure.story('User')
@allure.title('Test create user')
def test_create_user(delete_user):
    response = petstore_api().post('/user', data=json.dumps(Users.user_for_test_create), headers={'Content-Type': 'application/json'})
    assert response.status_code == 200


@pytest.mark.positive
@allure.tag('api')
@allure.story('User')
@allure.title('Test delete user')
def test_delete_user(create_user):
    username = Users.user_for_test_delete['username']
    response = petstore_api().delete(f'/user/{username}')

    assert response.status_code == 200


@pytest.mark.negative
@allure.tag('api')
@allure.story('User')
@allure.title('Test delete user(negative)')
def test_delete_user_negative():
    username = Users.user_for_test_delete['username']
    response = petstore_api().delete(f'/user/{username}')

    assert response.status_code == 404






@pytest.mark.positive
@allure.tag('api')
@allure.story('User')
@allure.title('Test update user')
def test_update_user(create_user):
    username = Users.user_for_test_create['username']
    response = petstore_api().put(f'/user/{username}', data=json.dumps(Users.user_for_test_update), headers={'Content-Type': 'application/json'})

    print(response.text)
    assert response.status_code == 200


@pytest.mark.skip
@pytest.mark.negative
@allure.tag('api')
@allure.story('User')
@allure.title('Test update user(User not exist)')
def test_update_user(create_user):
    username = Users.user_for_test_update['username']
    response = petstore_api().put(f'/user/{username}', data=json.dumps(Users.user_for_test_update), headers={'Content-Type': 'application/json'})

    print(response.text)
    assert response.status_code == 200



@pytest.mark.positive
@allure.tag('api')
@allure.story('User')
@allure.title('Test login (positive))')
def test_login_positive():
    pass
    # username = Users.user_for_test_update['username']
    # response = petstore_api().put(f'/user/{username}', data=json.dumps(Users.user_for_test_update), headers={'Content-Type': 'application/json'})
    #
    # print(response.text)
    # assert response.status_code == 200

@pytest.mark.negative
@allure.tag('api')
@allure.story('User')
@allure.title('Test login (negative)')
def test_login_negative():
    pass
# username = Users.user_for_test_update['username']
# response = petstore_api().put(f'/user/{username}', data=json.dumps(Users.user_for_test_update), headers={'Content-Type': 'application/json'})
#
# print(response.text)
# assert response.status_code == 200

@pytest.mark.positive
@allure.tag('api')
@allure.story('User')
@allure.title('Test logout')
def test_logout():
    pass
# username = Users.user_for_test_update['username']
# response = petstore_api().put(f'/user/{username}', data=json.dumps(Users.user_for_test_update), headers={'Content-Type': 'application/json'})
#
# print(response.text)
# assert response.status_code == 200

@pytest.mark.positive
@allure.tag('api')
@allure.story('User')
@allure.title('Test User Schema')
def test_user_schema():
    pass