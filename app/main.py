from fastapi import FastAPI

from app.routes import stock_price

import os
import logging

env = os.getenv("ENV")
version_endpoint = os.getenv("VERSION_ENDPOINT")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI(
    title="LAB Stock Price API",
    description="Application for delivering stock prices from Alpha Vantage.",
    version="1.0.0",
    contact={
        "name": "Anna Carpinello",
        "email": "anna.j.carpinello@gmail.com",
    },
    docs_url="/v1/docs",
)


@app.get('/', include_in_schema=False)
async def root():
    return {'message': f'Welcome to the LAB Stock Price API in the {env} environment.'}

app.include_router(stock_price.router, prefix=version_endpoint)
logger.info("Routers included")
