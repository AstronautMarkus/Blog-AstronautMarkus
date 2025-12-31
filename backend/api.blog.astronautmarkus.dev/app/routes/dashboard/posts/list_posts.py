from flask import Blueprint, render_template
from . import posts_bp
from app.models import Post

@posts_bp.route('/')
def list_posts():
    posts = Post.query.all()
    return render_template('dashboard/posts/list_posts.html', posts=posts)