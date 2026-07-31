import os
from app import create_app, db
from app.models.user import User
from flask_migrate import upgrade

def init_system(admin_password='admin'):
    app = create_app(os.getenv('FLASK_CONFIG') or 'dev')
    with app.app_context():
        print("Running database migrations...")
        upgrade()
        print("Migrations complete.")

        print("Checking for admin user...")
        admin = User.query.filter_by(username='admin').first()
        if not admin:
            print("Creating admin user...")
            admin = User(username='admin')
            admin.set_password(admin_password)
            db.session.add(admin)
            db.session.commit()
            print(f"Admin user created. Username: admin, Password: {admin_password}")
        else:
            print("Admin user already exists.")

if __name__ == '__main__':
    # You can change the default password here or pass it as an arg
    init_system(admin_password='change-this-password')
