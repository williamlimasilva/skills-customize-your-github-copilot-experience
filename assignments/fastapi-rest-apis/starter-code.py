"""
FastAPI REST API Starter Code

This is a basic template to get you started building a REST API with FastAPI.
Follow the assignment tasks to implement the required functionality.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# TODO: Define a Pydantic model for Item
# The model should have fields: id, name, description


# TODO: Create a simple in-memory storage for items
# You can use a list or dictionary to store items


# TODO: Implement GET /items endpoint
# This should return all items in the collection


# TODO: Implement GET /items/{item_id} endpoint
# This should return a single item by ID or raise a 404 error if not found


# TODO: Implement POST /items endpoint
# This should accept item data and add it to the collection


# TODO: Implement DELETE /items/{item_id} endpoint
# This should remove an item by ID


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
