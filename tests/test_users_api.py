from utils.logger import log_info
from utils.schema_validator import validate_schema
from utils.api_helper import get_request, post_request

def test_get_all_users():
    response = get_request('/users')
    assert response.status_code == 200
    data = response.json()
    log_info(f"Total Users Retrieved: {len(data)}")

    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "email": {"type": "string"},
                "username": {"type": "string"}
            },
            "required": ["id", "email", "username"]
        }
    }

    assert validate_schema(data,schema)

def test_create_user():
    payload = {
        "email": "masked_user@domain.com",
        "username": "test_user",
        "password": "********"
    }

    response = post_request('/users',payload)
    assert response.status_code in [200,201]