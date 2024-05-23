# Series Project

A Django-based project for managing time series data with a REST API.

## Description

This project provides a simple time series data store with a REST API. It includes features such as data ingestion, filtering, pagination, enhanced responses, and more.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or higher
- PostgreSQL (for production use)
- Redis (for caching)

### Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/series_project.git
    cd series_project
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```sh
    python manage.py migrate
    ```

5. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

## Usage

### Data Ingestion

To ingest data, run the custom management command:

  ```sh
  python manage.py ingest_data
  ```

### API Endpoints

#### Financial Data Endpoints

- **List Financial Data**
  - URL: `/financial-data/`
  - Method: `GET`
  - Description: Retrieve a list of financial data with pagination and filtering.
  - Parameters:
    - `page`: Page number for pagination.
    - `page_size`: Number of items per page.
    - `search`: Search term to filter results.
    - `date`: Filter by date.
    - `daily_customers`: Filter by daily customers.

- **Create Financial Data**
  - URL: `/financial-data/`
  - Method: `POST`
  - Description: Create a new financial data entry.
  - Body:
    ```json
    {
      "date": "YYYY-MM-DD",
      "daily_revenue": 1200.0,
      "daily_customers": 180,
      "tacos_sold": 250,
      "drinks_sold": 120,
      "total_employee_hours": 25
    }
    ```

- **Retrieve Financial Data**
  - URL: `/financial-data/<id>/`
  - Method: `GET`
  - Description: Retrieve a specific financial data entry.

- **Update Financial Data**
  - URL: `/financial-data/<id>/`
  - Method: `PUT`
  - Description: Update a specific financial data entry.
  - Body:
    ```json
    {
      "date": "YYYY-MM-DD",
      "daily_revenue": 1100.0,
      "daily_customers": 160,
      "tacos_sold": 210,
      "drinks_sold": 110,
      "total_employee_hours": 21
    }
    ```

- **Delete Financial Data**
  - URL: `/financial-data/<id>/`
  - Method: `DELETE`
  - Description: Delete a specific financial data entry.

### Running Tests

To run the tests, use the following command:

  ```sh
  python manage.py test seriesapp
  ```

## Features

- **Custom Pagination**: Configurable pagination with metadata.
- **Enhanced Error Handling**: Custom error responses for better client-side handling.
- **Caching**: Using Redis for caching to improve performance.
- **Search and Filtering**: Advanced search and filtering capabilities on list endpoints.