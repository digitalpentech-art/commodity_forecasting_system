from app import db
from app.models.audit import AuditLog
from flask_login import current_user

def log_action(action):
    user_id = current_user.id if current_user.is_authenticated else None
    log = AuditLog(user_id=user_id, action=action)
    db.session.add(log)
    db.session.commit()
