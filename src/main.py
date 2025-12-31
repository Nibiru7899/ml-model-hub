# Import necessary libraries
from flask import Flask, jsonify
import psycopg2
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create a new Flask application
app = Flask(__name__)

# Define a route for the root of the application
@app.route('/')
def home():
    # Return a JSON response
    return jsonify({'message': 'Welcome to the Learning Project'})

# Run the application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)