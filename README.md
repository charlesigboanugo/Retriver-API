# Retriver-API

RetriverAPI is a simple Django-based API that returns a JSON response containing an email address, the current date and time, and the project's GitHub repository URL.

## Features
- Responds to `GET` requests with a JSON object.
- Returns the current date and time dynamically.
- Provides the project’s GitHub repository URL.

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python (>= 3.8)
- Django
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/RetriverAPI.git
   cd RetriverAPI

2. Create a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate   # On Windows use:venv\Scripts\activate\

3. Install dependencies:
    pip install -r requirements.txt

4. Run Migrations
    python manage.py migrate

5. Start the development server:
    python manage.py runserver

The API will be accessible at http://127.0.0.1:8000/.


# API Documentation

## Endpoint
    GET /
    Base URL:

        Production: https://retriver-api.onrender.com/
        Local: http://127.0.0.1:8000/
    Request
        Method: GET
        Headers: NoNE
        Body: None
    Response
        Status: 200 OK
        Content-Type: application/json
    Example response:
        {
            "email": "your-email@example.com",
            "current_datetime": "2025-01-31T14:30:00Z",
            "github_url": "https://github.com/yourusername/RetriverAPI"
        }

    Example Usage
        curl -X GET https://retriver-api.onrender.com/

## Hire a Django Developer
Looking for skilled Django and Python developers? Check out: https://hng.tech/hire/python-developers