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

@posts_bp.route('/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.description = request.form.get('description')
        post.url = request.form.get('url')
        post.image_url = request.form.get('image_url')
        post.slug = slugify(post.title)
        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('posts.list_posts'))
    return render_template('dashboard/posts/edit_post.html', post=post)
