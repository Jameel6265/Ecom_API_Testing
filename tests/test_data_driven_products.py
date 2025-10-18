import pandas as pd
from utils.api_helper import post_request

# Function to read Excel data
def read_excel_data(file_path):
    df = pd.read_excel(file_path)  # Requires openpyxl
    for _, row in df.iterrows():
        yield row.to_dict()

# Test function
def test_create_products_from_excel():
    for product in read_excel_data('data/products.xlsx'):
        response = post_request('/products', product)
        assert response.status_code in [200, 201]
