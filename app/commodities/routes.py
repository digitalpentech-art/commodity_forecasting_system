from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.models.commodity import Category, Commodity
from app.forms.crud_forms import CommodityForm

commodities_bp = Blueprint('commodities', __name__)

@commodities_bp.route('/commodities', methods=['GET'])
@login_required
def list_commodities():
    commodities = Commodity.query.all()
    return render_template('commodities/list.html', commodities=commodities)

@commodities_bp.route('/commodities/add', methods=['GET', 'POST'])
@login_required
def add_commodity():
    form = CommodityForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]
    if form.validate_on_submit():
        new_commodity = Commodity(name=form.name.data, category_id=form.category_id.data, unit=form.unit.data)
        db.session.add(new_commodity)
        db.session.commit()
        flash('Commodity added successfully')
        return redirect(url_for('commodities.list_commodities'))
    return render_template('commodities/add.html', form=form)
