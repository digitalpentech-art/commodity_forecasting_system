from flask import Blueprint, render_template
from flask_login import login_required
from app.models.commodity import Commodity
from app.models.market import Market
from app.models.price import HistoricalPrice

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def index():
    stats = {
        'commodities': Commodity.query.count(),
        'markets': Market.query.count(),
        'prices': HistoricalPrice.query.count()
    }
    return render_template('dashboard/index.html', stats=stats)
