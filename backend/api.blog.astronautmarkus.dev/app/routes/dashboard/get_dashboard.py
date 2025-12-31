from flask import Blueprint, render_template
from app.middleware.checkUserAuth import login_required
from . import dashboard_bp
from app.models import Post

@dashboard_bp.route('')
@login_required
def dashboard_index():
    posts = [post.to_dict() for post in Post.query.all()]
    return render_template('dashboard/dashboard_home.html', posts=posts)
