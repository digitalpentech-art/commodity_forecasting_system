from app import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    commodities = db.relationship('Commodity', backref='category', lazy='dynamic')

class Commodity(db.Model):
    __tablename__ = 'commodities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    unit = db.Column(db.String(32), nullable=False)
    historical_prices = db.relationship('HistoricalPrice', backref='commodity', lazy='dynamic')
