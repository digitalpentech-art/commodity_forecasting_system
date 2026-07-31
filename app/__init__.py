from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.config.config import config_by_name

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_name='dev'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Register Blueprints
    from app.auth.routes import auth_bp
    from app.dashboard.routes import dashboard_bp
    from app.commodities.routes import commodities_bp
    from app.markets.routes import markets_bp
    from app.prices.routes import prices_bp
    from app.forecasting.routes import forecasting_bp
    from app.datasets.routes import datasets_bp
    from app.reports.routes import reports_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/')
    app.register_blueprint(commodities_bp, url_prefix='/')
    app.register_blueprint(markets_bp, url_prefix='/')
    app.register_blueprint(prices_bp, url_prefix='/')
    app.register_blueprint(forecasting_bp, url_prefix='/')
    app.register_blueprint(datasets_bp, url_prefix='/')
    app.register_blueprint(reports_bp, url_prefix='/')

    return app
