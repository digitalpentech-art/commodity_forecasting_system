from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.models.market import Market, LGA
from app.forms.crud_forms import MarketForm

markets_bp = Blueprint('markets', __name__)

@markets_bp.route('/markets', methods=['GET'])
@login_required
def list_markets():
    markets = Market.query.all()
    return render_template('markets/list.html', markets=markets)

@markets_bp.route('/markets/add', methods=['GET', 'POST'])
@login_required
def add_market():
    form = MarketForm()
    form.lga_id.choices = [(l.id, l.name) for l in LGA.query.all()]
    if form.validate_on_submit():
        new_market = Market(name=form.name.data, lga_id=form.lga_id.data)
        db.session.add(new_market)
        db.session.commit()
        flash('Market added successfully')
        return redirect(url_for('markets.list_markets'))
    
    return render_template('markets/add.html', form=form)
