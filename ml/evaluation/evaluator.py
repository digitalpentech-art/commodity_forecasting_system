import joblib
import os
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from ml.preprocessing.data_processor import get_data_as_dataframe, preprocess_data
from sklearn.model_selection import train_test_split

def evaluate_model():
    """Evaluates the trained model."""
    model_path = os.path.join('ml', 'saved_models', 'commodity_model.pkl')
    if not os.path.exists(model_path):
        return "Model not found."
    
    model = joblib.load(model_path)
    df = get_data_as_dataframe()
    df = preprocess_data(df)
    
    X = df[['commodity_id', 'market_id', 'day_of_week', 'month']]
    y = df['price']
    
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    predictions = model.predict(X_test)
    
    metrics = {
        'MAE': mean_absolute_error(y_test, predictions),
        'RMSE': mean_squared_error(y_test, predictions, squared=False),
        'R2': r2_score(y_test, predictions)
    }
    return metrics
