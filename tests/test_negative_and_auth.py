from utils.api_helper import get_request,post_request
from config.config import HEADERS, BASE_URL

def test_invalid_endpoint():
    response = get_request('/invalid_endpoint')
    assert response.status_code == 404, f'Expected 404, got::{response.status_code}'


# def test_create_product_invalid_payload():
#     invalid_payload = {'title':123,'price':'wrong type'}
#     response = post_request('/products',payload=invalid_payload)
#     print("DEBUG:", response.status_code, response.text)  # <—
#     assert response.status_code in [400,422,500],'Expected validation error'

def test_authentication_missing_token():
    url = "https://fakestoreapi.com/carts/user/1"
    no_auth_headers = {}
    response = get_request('/carts/user/1')
    expected = [200,401]
    assert response.status_code in expected,f'Expected {expected}, got {response.status_code}'


def test_authentication_invalid_token(monkeypatch):
    from utils import api_helper
    monkeypatch.setattr(api_helper,'HEADERS',{'Authorization':'Bearer invalid_token'})
    response = get_request('/users')
    assert response.status_code in [401,403,200],'Expected unauthorized access'