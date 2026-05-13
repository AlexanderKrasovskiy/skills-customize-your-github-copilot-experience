# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API using the FastAPI framework. Practice defining routes, using path and query parameters, accepting JSON request bodies, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create REST API Endpoints

#### Description
Build an API with several endpoints that demonstrate path parameters, query parameters, and POST request bodies.

#### Requirements
Completed program should:

- Use `FastAPI` to create a web application instance
- Define a `GET /` endpoint that returns a welcome message
- Define a `GET /items/{item_id}` endpoint that returns the requested item ID and optional query parameter data
- Define a `GET /sum` endpoint that accepts two query parameters and returns their sum
- Define a `POST /items/` endpoint that accepts a JSON body and returns the created item details
- Define a `POST /users/` endpoint that accepts a JSON body and returns the created user details

### 🛠️ Run and Test the API

#### Description
Run the FastAPI app locally with Uvicorn and test the endpoints using a browser or API client.

#### Requirements
Completed assignment should:

- Start the app with `uvicorn starter-code:app --reload`
- Use sample requests to verify API responses
- Return JSON responses for every endpoint
- Use clear field names and structured output
