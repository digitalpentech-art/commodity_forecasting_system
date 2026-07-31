# Commodity Forecasting System

A production-quality system for monitoring and forecasting national commodity prices.

## Features
- Secure Authentication & Role-Based Access Control
- Commodity & Market Management
- Historical Price Tracking (Manual & Bulk Import)
- Machine Learning Pipeline with XGBoost (for supported environments)
- Dashboard & Data Visualization
- REST API

## Installation
The system is designed for containerized deployment using Docker.

1. Ensure Docker and Docker Compose are installed.
2. Clone the repository: `git clone <repository_url>`
3. Run the application: `docker-compose up --build`

## Configuration
Update `docker-compose.yml` to set your environment variables (SECRET_KEY, DATABASE_URL, etc.).

## Documentation
- `docs/ARCHITECTURE.md` - System design
- `docs/ADMIN_MANUAL.md` - Administrative tasks
- `docs/USER_MANUAL.md` - End-user usage
