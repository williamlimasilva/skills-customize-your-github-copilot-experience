# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build scalable and efficient REST APIs using the FastAPI framework. You will practice creating endpoints, handling HTTP requests and responses, and working with data validation using Pydantic models.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Build a simple REST API with FastAPI that manages a collection of items. Create endpoints to retrieve all items, get a specific item by ID, and create new items.

#### Requirements
Completed program should:

- Set up a FastAPI application with a basic `GET /items` endpoint that returns a list of sample items.
- Implement a `GET /items/{item_id}` endpoint that retrieves a single item by its ID.
- Create a `POST /items` endpoint that accepts JSON data and adds a new item to the collection.
- Use Pydantic models to define the structure of items with fields like `id`, `name`, and `description`.
- Example usage:
  ```bash
  GET /items
  # Returns: [{"id": 1, "name": "Item 1", "description": "..."}]
  
  GET /items/1
  # Returns: {"id": 1, "name": "Item 1", "description": "..."}
  
  POST /items
  # Body: {"name": "New Item", "description": "..."}
  # Returns: {"id": 2, "name": "New Item", "description": "..."}
  ```

### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance the API with proper data validation, error handling, and HTTP status codes to provide clear feedback to clients.

#### Requirements
Completed program should:

- Use Pydantic models to validate incoming request data.
- Return appropriate HTTP status codes (e.g., 200 for success, 201 for resource created, 404 for not found, 400 for bad request).
- Handle cases where an item is not found and return a 404 error with a descriptive message.
- Validate that item names are not empty and have a reasonable length.
- Include a `DELETE /items/{item_id}` endpoint that removes an item and returns a 204 No Content response.
- Test the API using the interactive Swagger UI at `/docs`.
