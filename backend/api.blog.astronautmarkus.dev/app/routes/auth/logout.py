from flask import jsonify, request, make_response, redirect, url_for
from app.models import Session, db
from . import auth_bp

@auth_bp.route('/logout', methods=['POST'])
def logout():
    token = request.cookies.get('session_token')
    if token:
        session = Session.query.filter_by(token=token, is_active=True).first()
        if session:
            session.is_active = False
            db.session.commit()
    response = make_response(redirect(url_for('auth.login_form')))
    response.delete_cookie('session_token')
    return response
