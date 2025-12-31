from . import posts_bp
from flask import jsonify
from app.models import Post, PostView

@posts_bp.route('/', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    posts_data = []
    for post in posts:
        post_views = PostView.query.filter_by(post_id=post.id).all()
        posts_data.append({
            'id': post.id,
            'title': post.title,
            'description': post.description,
            'image_url': post.image_url,
            'slug': post.slug,
            'url': post.url,
            'views_count': len(post_views)
        })
    return jsonify(posts_data)

@posts_bp.route('/<string:slug>', methods=['GET'])
def get_post_by_slug(slug):
    post = Post.query.filter_by(slug=slug).first()

    if not post:
        return jsonify({'error': 'Post not found'}), 404

    post_id = post.id
    post_views = PostView.query.filter_by(post_id=post_id).all()

    post_data = {
        'id': post.id,
        'title': post.title,
        'description': post.description,
        'image_url': post.image_url,
        'slug': post.slug,
        'url': post.url,
        'views_count': len(post_views)
    }
    return jsonify(post_data)