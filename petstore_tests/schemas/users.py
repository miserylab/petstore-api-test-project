__author__ = 'miserylab'
from voluptuous import ALLOW_EXTRA
from voluptuous import Schema


user = Schema(
        {
        'id': int,
        'username': str,
        'firstName': str,
        'lastName': str,
        'email': str,
        'password': str,
        'phone': str,
        'userStatus': int}
    #     ,
    # extra=ALLOW_EXTRA
)

# user_for_test_create = {
#         "id": 12323424,
#         "username": "test1",
#         "firstName": "Test",
#         "lastName": "Create",
#         "email": "str@mail.com",
#         "password": "2222222",
#         "phone": "+32131311323",
#         "userStatus": 0
# }

# "User":{
#       "type":"object",
#       "properties":{
#          "id":{
#             "type":"integer",
#             "format":"int64"
#          },
#          "username":{
#             "type":"string"
#          },
#          "firstName":{
#             "type":"string"
#          },
#          "lastName":{
#             "type":"string"
#          },
#          "email":{
#             "type":"string"
#          },
#          "password":{
#             "type":"string"
#          },
#          "phone":{
#             "type":"string"
#          },
#          "userStatus":{
#             "type":"integer",
#             "format":"int32",
#             "description":"User Status"
#          }
#       },
#       "xml":{
#          "name":"User"
#       }
