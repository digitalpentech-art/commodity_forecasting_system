from app import db, create_app
from app.models.dataset import Dataset

app = create_app()
with app.app_context():
    new_dataset = Dataset(filename='wfp_food_prices_nga (1).csv')
    db.session.add(new_dataset)
    db.session.commit()
    print("Dataset registered successfully.")
