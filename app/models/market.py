from app import db

class State(db.Model):
    __tablename__ = 'states'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    lgas = db.relationship('LGA', backref='state', lazy='dynamic')

class LGA(db.Model):
    __tablename__ = 'lgas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'), nullable=False)
    markets = db.relationship('Market', backref='lga', lazy='dynamic')

class Market(db.Model):
    __tablename__ = 'markets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    lga_id = db.Column(db.Integer, db.ForeignKey('lgas.id'), nullable=False)
    historical_prices = db.relationship('HistoricalPrice', backref='market', lazy='dynamic')
