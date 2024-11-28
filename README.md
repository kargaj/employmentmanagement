# Simple Web App

This is a simple web application that uses a Django backend, a PostgreSQL database, and a Vue.js frontend. The application is fully dockerized and can be easily set up and run using Docker Compose.

- **Backend**: Django REST Framework (DRF) for handling API requests.
- **Database**: PostgreSQL as the database.
- **Frontend**: Vue.js with Vuetify and Vue Router.
- **Communication**: The frontend communicates with the backend through API endpoints.
- **Containerization**: Dockerized setup for easy deployment and local development.
  
## Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Setup Instructions

### 1. Build the Docker Images
Before running the application for the first time, build the Docker images:
```bash
docker-compose build
```

### 2. Start the Application

To start the application, use the following command:
```bash
docker-compose up
```

### 3. Access the Application
- **Frontend**:Open your browser and navigate to http://localhost:3000.
- **Backend**: The API is available at http://localhost:8000.

## Development Environment

The current setup is tailored only for development purposes. It includes:
- Debug mode enabled for the Django backend.
- Development Vue.js server running on port 3000.
- Local PostgreSQL database for testing and development.
- Docker Compose configuration designed for ease of development.

## Tests
### Backend unit tests
Backend unit tests are written in Python using `pytest`.

### To-Do: Frontend Testing with Playwright
End-to-end testing for the frontend using Playwright is planned for future implementation.

## API Documentation

The backend provides a RESTful API at the `/employers` endpoint to manage employment data. 
### Employer Fields

| Field Name   | Type     | Description                | Read-Only |
|--------------|----------|----------------------------|-----------|
| `id`         | Integer  | Unique identifier          | Yes       |
| `name`       | String   | Name of the employer       | No        |
| `birth_date` | Date   | Date of birth   | No        |
| `department` | String   | Employer's department (possible choices: "HR", "DEV", "S&M", if other - `None`) | No        |
| `department_fullname` | String | Full name of department | Yes       |
| `age` | Integer | Age of the employer     | Yes       |


### Supported Methods
- **`GET`**: Retrieve a list of all employers or a single employer.
- **`POST`**: Create a new employer.
- **`PUT`**: Update an existing employer.
- **`PATCH`**: Partially update an existing employer.
- **`DELETE`**: Delete an employer.

