__author__ = 'miserylab'

import pytest
from pytest_voluptuous import S
from petstore_tests.schemas.users import user
from petstore_tests.utils.sessions import reqres_api


def test_users_count_on_page():
    '''
    1. get https://reqres.in/api/users?page=2
    2. asserts
    '''
    page = 2
    users_per_page = 6
    response = reqres_api().get('/users', params={'page': page})

    assert len(response.json()['data']) == users_per_page


def test_get_users_status_code():
    '''
    1. get https://reqres.in/api/users?page=2
    2. asserts
    '''
    page = 2
    response = reqres_api().get('/users', params={'page': page})

    assert response.status_code == 200


def test_get_user_fields_validation():
    '''
    1. get https://reqres.in/api/users/1
    2. asserts
    '''
    response = reqres_api().get("/users/1")

    assert isinstance(response.json()['data']['id'], int)
    assert isinstance(response.json()['data']['email'], str)
    assert isinstance(response.json()['data']['first_name'], str)
    assert isinstance(response.json()['data']['last_name'], str)
    assert isinstance(response.json()['data']['avatar'], str)


def test_get_user_schema_validation():
    response = reqres_api().get('/users/1')

    assert S(user) == response.json()



test_data = [(1, "Bluth"), (2, "Weaver")]

@pytest.mark.parametrize("id, expected_last_name", test_data)
def test_get_user_for_check_last_name(id, expected_last_name):
    response = reqres_api().get(f'/users/{id}')
    assert response.json()['data']["last_name"] == expected_last_name

