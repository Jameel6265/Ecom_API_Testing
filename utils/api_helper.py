import requests
from config.config import BASE_URL,HEADERS
from utils.logger import log_info, log_error


def get_request(endpoint):
    url = f'{BASE_URL}{endpoint}'
    log_info(f'GET REQUEST::{url}')
    response = requests.get(url,headers=HEADERS)
    return response

def post_request(endpoint,payload):
    url = f'{BASE_URL}{endpoint}'
    log_info(f"POST Request::{url}, Payload: {str(payload)[:100]}")
    response = requests.post(url,json=payload,headers=HEADERS)
    return response

def put_request(endpoint,payload):
    url = f'{BASE_URL}{endpoint}'
    log_info(f'PUT Request: {url}, Payload: {str(payload)[:100]}')
    response = requests.put(url,json=payload,headers=HEADERS)
    return response

def delete_request(endpoint):
    url = f'{BASE_URL}{endpoint}'
    log_info(f"DELETE Request: {url}")
    response = requests.delete(url,headers=HEADERS)
    return response