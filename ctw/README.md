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
edit docker-compose.yml: put your API key for fetching data from AlphaVantage. [API_KEY=V1EVWNVF2T9UVPIN]
docker compose up
```
API Document: https://localhost:5000/docs

## how to maintain the API key to retrieve financial data from AlphaVantage in both local development and production environment:
API keys for different environment can be stored in some key management services like 1password.


## Requirements:

- The program should be written in Python 3.
- You are free to use any API and libraries you like, but should include a brief explanation of why you chose the API and libraries you used in README.
- The API key to retrieve financial data should be stored securely. Please provide a description of how to maintain the API key from both local development and production environment in README.
- The database in Problem Statement 1 could be created using SQLite/MySQL/.. with your own choice.
- The program should include error handling to handle cases where the API returns an error or the data is not in the correct format.
- The program should cover as many edge cases as possible, not limited to expectations from deliverable above.
- The program should use appropriate data structures and algorithms to store the data and perform the calculations.
- The program should include appropriate documentation, including docstrings and inline comments to explain the code.

## Evaluation Criteria:

Your solution will be evaluated based on the following criteria:

- Correctness: Does the program produce the correct results?
- Code quality: Is the code well-structured, easy to read, and maintainable?
- Design: Does the program make good use of functions, data structures, algorithms, databases, and libraries?
- Error handling: Does the program handle errors and unexpected input appropriately?
- Documentation: Is the code adequately documented, with clear explanations of the algorithms and data structures used?

## Additional Notes:

You have 7 days to complete this assignment and submit your solution.
