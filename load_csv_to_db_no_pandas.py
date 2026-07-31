import csv
from app import db, create_app
from app.models.price import HistoricalPrice
from datetime import datetime
import os

app = create_app('dev')
with app.app_context():
    with open('data/uploads/wfp_food_prices_nga (1).csv', 'r') as f:
        reader = csv.DictReader(f)
        # Skip the second header row (the one with #date, #adm1+name, etc.)
        next(reader)
        
        for row in reader:
            try:
                price_entry = HistoricalPrice(
                    commodity_id=int(row['commodity_id']),
                    market_id=int(row['market_id']),
                    price=float(row['price']),
                    date=datetime.strptime(row['date'], '%Y-%m-%d')
                )
                db.session.add(price_entry)
            except (ValueError, TypeError):
                continue # Skip malformed rows
                
        db.session.commit()
        print("Data loaded into database successfully using csv module.")
