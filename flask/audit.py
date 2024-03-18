from datetime import datetime
from flask import request
from app import db
from models import AuditLog

def log_access(user_id, action):
    new_log = AuditLog(user_id=user_id, action=action, timestamp=datetime.now(), ip_address=request.remote_addr)
    db.session.add(new_log)
    db.session.commit()
