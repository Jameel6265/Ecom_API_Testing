import csv
from utils.api_helper import post_request

def read_csv_data(file_path):
    with open(file_path,newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            yield row

def test_create_products_from_csv():
    for product in read_csv_data('data/products.csv'):
        response = post_request('/products',product)
        assert response.status_code in [200,201]