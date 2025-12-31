from flask import request, render_template, redirect, url_for, flash
from app import db
from app.models import User
from app import config
from . import auth_bp
from werkzeug.security import generate_password_hash

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    errors = {}
    values = {}
    if request.method == 'POST':
        data = request.form
        required_fields = ['username', 'email', 'password', 'confirm_password']

        for field in required_fields:
            values[field] = data.get(field, '')

        for field in required_fields:
            if not data.get(field):
                errors[field] = f'The field {field} is required.'

        if data.get('password') and data.get('confirm_password'):
            if data['password'] != data['confirm_password']:
                errors['confirm_password'] = 'Passwords do not match.'

        if data.get('email'):
            if User.query.filter_by(email=data['email']).first():
                errors['email'] = 'The email is already registered.'
        if data.get('username'):
            if User.query.filter_by(username=data['username']).first():
                errors['username'] = 'The username is already taken.'

        if not errors:
            hashed_password = generate_password_hash(data['password'])
            new_user = User(
                username=data['username'],
                email=data['email'],
                password=hashed_password
            )
            db.session.add(new_user)
            db.session.commit()

            flash('User registered successfully. Please log in.', 'success')
            return redirect(url_for('auth.login_form'))

        return render_template('register.html', errors=errors, values=values)

    return render_template('register.html', errors=errors, values=values)