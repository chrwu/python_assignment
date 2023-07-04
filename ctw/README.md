# Description
This project aims to build a simple backend service to provide APIs for users to get stock information.
Three APIs are implemented (Two are required).
- /fincancail_data: returns stock information for a given period and conditions.
- /statistics: returns average stock information for a given period.
- /ingest_data: allows users to ingest stock information they want.

Project structure:
```
ctw/
├── model.py: Define Tables and DB engine
├── schemas.py: Define API Response Schemas
├── get_raw_data.py: Contains a function to fetch raw data from AlphaVantage, and a function to ingest data into postgres
├── Dockerfile: Containerize our code.
├── docker-compose.yml: Define two services: web backend and postgres database
├── README.md
├── requirements.txt: Required libraries
└── financial/api.py: Define APIs

```

## Tech stack
FastAPI, SQLAlchemy, Postgres, docker/docker-compose
 

## How to run your code in local environment
```
cd ctw
edit docker-compose.yml: put your API key for fetching data from AlphaVantage.
docker compose up
```
API Document: https://localhost:5000/docs

## how to maintain the API key to retrieve financial data from AlphaVantage in both local development and production environment:
API keys for different environment can be stored in some key management services like 1password.


