from fastapi import APIRouter, Query, Depends, HTTPException, Path
from app.authentication.auth_api_key import get_api_key
import requests
import logging

router = APIRouter()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

alpha_vantage_url = "https://www.alphavantage.co/query"


def fetch_stock_price(symbol: str, api_key: str):
    response = requests.get(alpha_vantage_url, params={
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': api_key
    })

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail='Error fetching stock data from Alpha Vantage')

    data = response.json()
    logger.info(f'Response body: {data}')

    if 'Error Message' in data:
        raise HTTPException(status_code=400, detail='Invalid API call')

    if 'Information' in data:
        raise HTTPException(status_code=429, detail='API call frequency limit reached')

    stock_price = data.get('Global Quote', {}).get('05. price')

    if stock_price is None:
        raise HTTPException(status_code=404, detail=f'Price not found for symbol {symbol}')

    return float(stock_price)


@router.get('/stocks')
async def get_stocks(ids: str = Query(..., description='List of stock ids prices needed for'),
                     api_key: str = Depends(get_api_key)):
    stock_ids = ids.split(',')
    stock_prices = {}
    for stock_id in stock_ids:
        try:
            stock_prices[stock_id] = fetch_stock_price(stock_id, api_key)
        except HTTPException as e:
            stock_prices[stock_id] = str(e.detail)

    return stock_prices


@router.get('/stocks/{id}')
async def get_stock(id: str = Path(..., description='Stock id price needed for'), api_key: str = Depends(get_api_key)):
    try:
        stock_price = fetch_stock_price(id, api_key)
        return {id: stock_price}
    except HTTPException as e:
        raise e
