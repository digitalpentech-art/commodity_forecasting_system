# Software Requirements Specification (SRS) - Updated for SQLite

## 1. Introduction
This system is designed to monitor, analyze, and forecast national commodity prices using an XGBoost-based machine learning model integrated with a robust Flask web application.

## 2. System Users (Roles)
- **Administrator**: Full system access, user management, system configuration.
- **Data Entry Officer**: Manual data entry for commodity prices.
- **Market Officer**: Management of market data (locations, types).
- **Researcher/Government Analyst**: Access to advanced analytics, reports, and forecasting tools.
- **Trader/Farmer**: View commodity price trends and forecasts.
- **Public User**: Read-only access to price trends.

## 3. Functional Modules
- **Authentication**: Secure registration, login, role-based access.
- **Dashboard**: Analytics, charts, summary of forecasts.
- **Commodity/Market Management**: CRUD operations for commodities and markets.
- **Historical Price Module**: Data entry, CSV/Excel import, validation.
- **Dataset Management**: Data cleaning, feature engineering, versioning.
- **Machine Learning Module**: Train, evaluate, deploy XGBoost models.
- **Forecast Module**: Prediction API for various time horizons.
- **Visualization/Reports**: Interactive charts and exportable reports.
- **Notifications/Audit**: Alerts and activity tracking.

## 4. Non-Functional Requirements
- **Security**: SQLi, XSS, CSRF protection, rate limiting, password hashing, HTTPS.
- **Performance**: Efficient model inference, responsive UI.
- **Maintainability**: Modular architecture, clear documentation, PEP 8 compliance.
- **Database**: SQLite for lightweight, file-based storage.
