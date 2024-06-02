import os
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

version = "v1"


def test_get_stocks():
    response = client.get(f'/{version}/stocks?ids=MSFT,AAPL')
    assert response.status_code == 200
    data = response.json()
    assert 'MSFT' in data
    assert 'AAPL' in data


def test_get_stock():
    response = client.get(f'/{version}/stocks/MSFT')
    assert response.status_code == 200
    data = response.json()
    assert 'MSFT' in data


def test_missing_stock_price():
    response = client.get(f'/{version}/stocks/NOPRICE')
    assert response.status_code == 404
    data = response.json()
    assert data['detail'] == 'Price not found for symbol NOPRICE'


def test_error_fetching_data():
    response = client.get('/SERVERERROR')
    assert response.status_code == 502
    data = response.json()
    assert data['detail'] == 'Error fetching data from Alpha Vantage'


def test_api_key_not_found():
    os.environ['API_KEY'] = ''
    response = client.get(f'/{version}/stocks/MSFT')
    assert response.status_code == 500
    data = response.json()
    assert data['detail'] == 'API key not found'
