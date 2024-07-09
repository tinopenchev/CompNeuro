import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse}")
    joblib.dump(model, 'models/linear_regression_model.pkl')

if __name__ == "__main__":
    data = pd.read_csv('data/features.csv')
    features = ['Feature1', 'Feature2']
    X = data[features]
    y = data['Target']
    train_model(X, y)

