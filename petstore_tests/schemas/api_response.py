from voluptuous import Schema

api_response = Schema(
    {
        'code': int,
        'type': str,
        'message': str
    }
)
