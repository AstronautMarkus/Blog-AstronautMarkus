from flask import request, redirect, url_for, render_template, flash
from . import posts_bp
from app.models import db, Post
import re

def slugify(text):
    # Simple slugify: lowercase, replace spaces with '-', remove non-alphanum
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = re.sub(r'^-+|-+$', '', text)
    return text

@posts_bp.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        url = request.form.get('url')
        image_url = request.form.get('image_url')
        slug = slugify(title)
        post = Post(title=title, description=description, url=url, image_url=image_url, slug=slug)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('posts.list_posts'))
    return render_template('dashboard/posts/create_post.html')
