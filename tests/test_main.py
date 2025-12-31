# Import necessary libraries
import pytest
from src.main import app

# Define a test for the root route
def test_home():
    # Create a test client
    client = app.test_client()
    # Make a GET request to the root route
    response = client.get('/')
    # Assert that the response is successful
    assert response.status_code == 200
    # Assert that the response is JSON
    assert response.is_json