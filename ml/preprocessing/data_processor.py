import pandas as pd
import numpy as np

from app.models.price import HistoricalPrice
from typing import Optional

def get_data_as_dataframe() -> pd.DataFrame:
    prices = HistoricalPrice.query.all()
    data = [{
        'date': p.date,
        'commodity_id': p.commodity_id,
        'market_id': p.market_id,
        'price': p.price
    } for p in prices]
    
    df = pd.DataFrame(data)
    if not df.empty:
        df['date'] = pd.to_datetime(df['date'])
    return df

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    
    df['day_of_week'] = df['date'].dt.dayofweek
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['day_of_year'] = df['date'].dt.dayofyear
    
    df = df.dropna()
    
    return df
