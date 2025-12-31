from flask import Blueprint, render_template
from app.middleware.checkUserAuth import login_required
from . import dashboard_bp

@dashboard_bp.route('/dashboard')
@login_required
def dashboard_index():
    return render_template('dashboard.html')
