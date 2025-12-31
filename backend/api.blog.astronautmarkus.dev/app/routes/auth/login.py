from flask import request, render_template, redirect, url_for, flash, make_response
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
from app.models import User, Session, db
from . import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login_form():
    error = None
    values = {}
    if request.method == 'POST':
        data = request.form
        username_or_email = data.get('username') or data.get('email')
        password = data.get('password')
        values['username'] = data.get('username', '')

        if not username_or_email or not password:
            error = 'Username/email and password are required.'
            return render_template('login.html', error=error, values=values)

        user = User.query.filter(
            (User.username == username_or_email) | (User.email == username_or_email)
        ).first()

        if not user or not check_password_hash(user.password, password):
            error = 'Invalid credentials.'
            return render_template('login.html', error=error, values=values)

        expires_at = datetime.utcnow() + timedelta(days=7)
        session = Session(user_id=user.id, expires_at=expires_at)
        db.session.add(session)
        db.session.commit()

        response = make_response(redirect(url_for('dashboard.dashboard_index')))
        response.set_cookie(
            'session_token',
            session.token,
            httponly=True,
            secure=True,
            samesite='Lax',
            expires=expires_at
        )
        flash('Login successful.', 'success')
        return response

    return render_template('login.html', error=error, values=values)
