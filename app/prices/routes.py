from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.models.price import HistoricalPrice
from app.models.commodity import Commodity
from app.models.market import Market

prices_bp = Blueprint('prices', __name__)

@prices_bp.route('/prices', methods=['GET'])
@login_required
def list_prices():
    prices = HistoricalPrice.query.all()
    return render_template('prices/list.html', prices=prices)

@prices_bp.route('/prices/add', methods=['GET', 'POST'])
@login_required
def add_price():
    if request.method == 'POST':
        commodity_id = request.form.get('commodity_id')
        market_id = request.form.get('market_id')
        price = request.form.get('price')
        
        new_price = HistoricalPrice(commodity_id=commodity_id, market_id=market_id, price=float(price))
        db.session.add(new_price)
        db.session.commit()
        flash('Price entry added successfully')
        return redirect(url_for('prices.list_prices'))
    
    commodities = Commodity.query.all()
    markets = Market.query.all()
    return render_template('prices/add.html', commodities=commodities, markets=markets)
