from utils.api_helper import get_request,post_request,put_request
from utils.schema_validator import validate_schema

def test_get_products():
    response = get_request('/products')
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data,list)
    assert len(data)>0

def test_create_product():
    payload = {
        "title": "Automation Test Product",
        "price": 19.99,
        "description": "Created via automation",
        "category": "electronics",
        "image": "https://i.pravatar.cc"
    }
    response = post_request('/products',payload)
    assert response.status_code in [200,201]
    data = response.json()
    assert data['title'] == 'Automation Test Product'

def test_update_product():
    payload={'price':25.99}
    response = put_request('/products/1',payload=payload)
    assert response.status_code==200