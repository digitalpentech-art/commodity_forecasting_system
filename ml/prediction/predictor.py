try:
    import joblib
    import pandas as pd
    import numpy as np
except ImportError:
    from ml.mock_ml import joblib, pd, np

import os
from typing import Optional

def load_model():
    """Loads the trained XGBoost model."""
    model_path = os.path.join('ml', 'saved_models', 'commodity_model.pkl')
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

def predict_price(commodity_id: int, market_id: int, day_of_week: int, month: int, year: int, day_of_year: int) -> Optional[float]:
    """
    Predicts the price for a commodity in a given market.
    
    Args:
        commodity_id (int): ID of the commodity.
        market_id (int): ID of the market.
        day_of_week (int): Day of the week (0-6).
        month (int): Month (1-12).
        year (int): Year (e.g., 2026).
        day_of_year (int): Day of the year (1-365).
        
    Returns:
        Optional[float]: Predicted price, or None if the model is not available.
    """
    model = load_model()
    if model is None:
        return None
    
    # Feature vector
    features = pd.DataFrame([[commodity_id, market_id, day_of_week, month, year, day_of_year]],
                             columns=['commodity_id', 'market_id', 'day_of_week', 'month', 'year', 'day_of_year'])
    
    prediction = model.predict(features)
    return float(prediction[0])
