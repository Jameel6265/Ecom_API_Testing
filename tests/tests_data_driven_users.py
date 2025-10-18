# tests/test_data_driven_users.py
import json
from utils.api_helper import post_request

def test_create_users_from_json():
    with open("data/users.json") as f:
        users = json.load(f)
    for user in users:
        response = post_request("/users", user)
        assert response.status_code in [200, 201]
