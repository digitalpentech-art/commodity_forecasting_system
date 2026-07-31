from flask import Blueprint, render_template, Response
from flask_login import login_required
from app.models.price import HistoricalPrice
from app.datasets.mock_pandas import pd

reports_bp = Blueprint('reports', __name__)

@reports_bp.route('/reports/dashboard', methods=['GET'])
@login_required
def dashboard_report():
    # Fetch data for charting
    prices = HistoricalPrice.query.all()
    data = [{'date': p.date, 'price': p.price} for p in prices]
    df = pd.DataFrame(data)
    
    # Simple aggregation for chart (e.g., average price by date)
    if not df.empty:
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
        chart_data = df.groupby('date')['price'].mean().to_dict()
    else:
        chart_data = {}
        
    return render_template('reports/dashboard.html', chart_data=chart_data)

@reports_bp.route('/reports/export', methods=['GET'])
@login_required
def export_report():
    prices = HistoricalPrice.query.all()
    data = [{'date': p.date, 'commodity': p.commodity.name, 'market': p.market.name, 'price': p.price} for p in prices]
    df = pd.DataFrame(data)
    return Response(
        df.to_csv(index=False), 
        mimetype='text/csv', 
        headers={"Content-Disposition": "attachment;filename=prices.csv"}
    )
