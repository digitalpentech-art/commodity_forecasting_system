from app import create_app
from app.models.price import HistoricalPrice

app = create_app('dev')
with app.app_context():
    print(f'Total prices: {HistoricalPrice.query.count()}')
