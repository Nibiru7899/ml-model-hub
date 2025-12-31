# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Define a class for the machine learning model
class LearningModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        # Train the model
        self.model.fit(X_train, y_train)
        # Return the trained model
        return self.model