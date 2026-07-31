from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CommodityForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    category_id = SelectField('Category', coerce=int, validators=[DataRequired()])
    unit = StringField('Unit', validators=[DataRequired()])
    submit = SubmitField('Add Commodity')

class MarketForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    lga_id = SelectField('LGA', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Add Market')
