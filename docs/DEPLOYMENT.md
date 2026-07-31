# Production Deployment Guide - Commodity Forecasting System

## 1. Environment Setup
1.  Copy the `template.env` to `.env`:
    `cp template.env .env`
2.  Edit `.env` and set your `SECRET_KEY` and `DATABASE_URL` (e.g., `sqlite:////data/data/com.termux/files/home/commodity_forecasting_system/instance/prod.db`).

## 2. Dependencies
Install production dependencies:
`pip install -r requirements.txt gunicorn`

## 3. Database Migration
Ensure the database is up to date:
`export FLASK_CONFIG=prod`
`flask db upgrade`

## 4. Run with Gunicorn
Use Gunicorn to serve the application:
`export FLASK_CONFIG=prod`
`gunicorn -w 1 -b 0.0.0.0:8000 "run:app"`

---
*Note: Using SQLite in production is suitable for low-traffic applications but may face limitations with concurrent writes.*
