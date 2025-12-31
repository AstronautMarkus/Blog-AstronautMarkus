from flask import redirect, url_for, flash
from . import posts_bp
from app.models import db, Post

@posts_bp.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('posts.list_posts'))
