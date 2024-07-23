# LatencyMockerDB

## Overview

DBLatencyTester is a tool designed to connect to a user’s database, mock data, and measure the latency between the service and the database. This tool helps in analyzing and profiling the performance of database operations.

## Features

- ~~Connect to multiple database types (e.g., MariaDB, MySQL, PostgreSQL, SQLite) COMING SOON~~ 
- Mock data generation for testing purposes
- Measure and report latency of database operations
- Configurable through YAML files for easy setup
- Generate csv to analyze the data with ALL TESTS

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/GustavoScardovelliSiqueroli/latency-mocker-db.git
    cd latency-mocker-db
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Edit a `config.yaml` file in the root directory of the project with the following structure:

```yaml
database:
  host: "localhost"
  user: "your_username"
  password: "your_password"
```

## Usage

1. Run the main script to start the latency tests:
    ```bash
    cd ./app
    python main.py
    ```

2. Enter how many columns you want to test and then how many rows to insert.

3. The results will be displayed in the console and saved to a CSV file with name "result.csv".

4. You can run as many as you want, it will add without deleting previous tests.


