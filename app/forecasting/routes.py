from flask import Blueprint, render_template, request, flash
from flask_login import login_required
from app.models.commodity import Commodity
from app.models.market import Market
from ml.prediction.predictor import predict_price
from datetime import datetime

forecasting_bp = Blueprint('forecasting', __name__)

@forecasting_bp.route('/forecast', methods=['GET', 'POST'])
@login_required
def forecast():
    prediction = None
    if request.method == 'POST':
        commodity_id = int(request.form.get('commodity_id'))
        market_id = int(request.form.get('market_id'))
        date_str = request.form.get('date')
        
        # Convert date to features
        date = datetime.strptime(date_str, '%Y-%m-%d')
        day_of_week = date.weekday()
        month = date.month
        
        prediction = predict_price(commodity_id, market_id, day_of_week, month)
        if prediction is None:
            flash('Model not trained yet.')
            
    commodities = Commodity.query.all()
    markets = Market.query.all()
    return render_template('forecasting/index.html', commodities=commodities, markets=markets, prediction=prediction)
