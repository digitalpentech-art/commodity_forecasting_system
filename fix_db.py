from app import db, create_app
app = create_app('dev')
with app.app_context():
    db.create_all()
    print("Tables created.")
