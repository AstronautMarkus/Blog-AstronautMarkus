from functools import wraps
from flask import request, jsonify, g
from app.models import Session
from datetime import datetime

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        token = None
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
        else:
            token = request.cookies.get('session_token')
        if not token:
            return jsonify({'error': 'Authorization token required.'}), 401
        session = Session.query.filter_by(token=token, is_active=True).first()
        if not session or session.expires_at < datetime.utcnow():
            return jsonify({'error': 'Invalid or expired session token.'}), 401
        g.current_user_id = session.user_id
        g.session = session
        return f(*args, **kwargs)
    return decorated_function
