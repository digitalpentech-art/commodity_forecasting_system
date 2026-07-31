import pandas as pd
from app import db, create_app
from app.models.price import HistoricalPrice
import os

app = create_app('dev')
with app.app_context():
    df = pd.read_csv('data/uploads/wfp_food_prices_nga (1).csv')
    
    # Process and load into database
    # Assuming columns: date, market_id, commodity_id, price
    for _, row in df.iterrows():
        price_entry = HistoricalPrice(
            commodity_id=row['commodity_id'],
            market_id=row['market_id'],
            price=row['price'],
            date=pd.to_datetime(row['date'])
        )
        db.session.add(price_entry)
    
    db.session.commit()
    print("Data loaded into database successfully.")
