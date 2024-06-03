# LAB Stock Price API

## Overview

The Stock Price API is a RESTful service built with FastAPI that allows users to retrieve current stock prices for given stock IDs using the Alpha Vantage API. This application provides two endpoints:

- `GET /stocks`: Fetches current prices for a list of stock IDs.
- `GET /stocks/{id}`: Fetches the current price for a single stock ID.

## Features

- Retrieve stock prices in real-time using the Alpha Vantage API.
- Handle multiple stock IDs in a single request.
- Robust error handling for invalid API keys and invalid stock symbols.
- Comprehensive unit tests to ensure the reliability and correctness of the API.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Requests

## Setup

### Clone the Repository

First, clone the repository to your local machine and get into the project:

```bash
git clone https://github.com/acarpinello/LAB-stock-price-api.git
cd LAB-stock-price-api
```

### Create and Activate a Virtual Environment
Create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies
Install the required dependencies using pip as well as the environment and version of the app. You can choose to 'deploy' dev, stg, or prd. 

```bash
pip install -r requirements.txt
source env/.env.{environment}
```

### Set Up Environment Variables
Set your Alpha Vantage API key as an environment variable:
```bash
export API_KEY=your_api_key_here
```
If you have not created an API_KEY, register for a free one from Alpha Vantage here, https://www.alphavantage.co/support/#api-key

### Running the API
Start the FastAPI server using Uvicorn:

```bash
uvicorn app.main:app --reload
```
The root of the API will be accessible at http://127.0.0.1:8000.

## How to Use the API
### Swagger Docs
Once your API is running, you can access the Swagger documentation at:

http://127.0.0.1:8000/v1/docs

This UI allows you to interact with the API endpoints, see the required parameters, and view example responses.

1. Select the drop-down arrow of the endpoint you wish to use, which are described in more detail below.
2. Select `Try it out`
3. Add the required query parameters and select `Execute`
4. You will receive a curl command of your request and associated request url along with a status code of your request and the response body containing the information you want. 

### Curl
You can also make an API request using curl or any HTTP client by specifying the stock IDs as query parameters as shown below. 

GET /stocks
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/v1/stocks?ids={list_of_ids}' \
  -H 'accept: application/json'
```
GET /stock
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/v1/stocks/{stock_id}' \
  -H 'accept: application/json'
```
## API Endpoints

### GET /stocks
Retrieve current prices for a list of stock IDs.

Request Example
```http
GET /stocks?ids=MSFT,AAPL,GOOGL
```

Response 
```json
{
  "MSFT": 250.45,
  "AAPL": 130.84,
  "GOOGL": 2390.12
}
```

### GET /stocks/{id}
Retrieve the current price for a single stock ID.

Request Example
```http
GET /stocks/MSFT
```

Response
```json
{
  "MSFT": 250.45
}
```

## Running Tests
Unit tests are included to ensure the correctness and reliability of the API endpoints. To run the tests, use pytest:

```bash
source env/.env.dev
export API_KEY=your_dev_api_key_here
pytest
```

NOTE: The standard API rate limit of Alpha Vantage is 25 requests per day for free API keys. If this rate limit is hit, it will cause tests to fail. 
