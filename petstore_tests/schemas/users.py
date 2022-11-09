__author__ = 'miserylab'
from voluptuous import ALLOW_EXTRA
from voluptuous import Schema

user = Schema(
        {
        'id': int,
        'email': str,
        'first_name': str,
        'last_name': str,
        'avatar': str},
    extra=ALLOW_EXTRA
)


# users = Schema({
#     'data': [user]
#     },
#     extra=ALLOW_EXTRA,
#     required=True
# )