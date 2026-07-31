try:
    import xgboost as xgb
    import joblib
    from sklearn.model_selection import train_test_split, GridSearchCV
except ImportError:
    from ml.mock_ml import xgb, joblib, sklearn
    train_test_split = sklearn.model_selection.train_test_split
    GridSearchCV = sklearn.model_selection.GridSearchCV

import os
from ml.preprocessing.data_processor import get_data_as_dataframe, preprocess_data
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def train_model():
    """
    Trains an XGBoost regressor with hyperparameter tuning and saves the best model.
    
    Returns:
        str: Path to the saved model file, or None if training failed.
    """
    df = get_data_as_dataframe()
    df = preprocess_data(df)
    
    if len(df) < 10:
        logger.warning("Not enough data to train.")
        return None

    # Features and Target
    X = df[['commodity_id', 'market_id', 'day_of_week', 'month', 'year', 'day_of_year']]
    y = df['price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Hyperparameter Tuning
    param_grid = {
        'n_estimators': [50, 100],
        'learning_rate': [0.01, 0.1],
        'max_depth': [3, 5]
    }
    
    xgb_model = xgb.XGBRegressor(objective='reg:squarederror')
    grid_search = GridSearchCV(estimator=xgb_model, param_grid=param_grid, cv=3, scoring='neg_mean_absolute_error')
    grid_search.fit(X_train, y_train)
    
    best_model = grid_search.best_estimator_
    
    # Save Model
    model_path = os.path.join('ml', 'saved_models', 'commodity_model.pkl')
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(best_model, model_path)
    
    logger.info(f"Best model saved to {model_path} with params: {grid_search.best_params_}")
    return model_path
