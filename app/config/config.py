import os

class Config:
    # WARNING: Hardcoded values used for testing purposes. 
    # Do not use these in production.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-for-testing-only'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///dev.db'

class ProductionConfig(Config):
    DEBUG = False
    # Fallback to local sqlite for testing if DATABASE_URL is not set
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///prod.db'
