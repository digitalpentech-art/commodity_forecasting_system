# Project Guidelines - Commodity Forecasting System

## Architecture
- Modular Flask application using Blueprints.
- XGBoost-based ML pipeline decoupled from the web application.
- Normalized PostgreSQL database with SQLAlchemy ORM.

## Coding Standards
- Adhere to PEP 8.
- Use meaningful variable/function names.
- Type hinting is mandatory for all functions and classes.
- Docstrings required for all modules, classes, and methods.

## Development Lifecycle
- Incrementally build, test, and integrate modules.
- Maintain comprehensive documentation.
- Prioritize security (SQLi, XSS, CSRF protection, rate limiting, hashing).
