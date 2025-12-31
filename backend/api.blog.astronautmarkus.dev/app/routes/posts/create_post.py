from . import posts_bp
from flask import request, jsonify
from app.models import Post
from app import db

@posts_bp.route('/', methods=['POST'])
def create_post():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    slug = data.get('slug')
    image_url = data.get('image_url')
    url = data.get('url')

    if not title or not description or not slug:
        return jsonify({'error': 'Missing required fields'}), 400

    # Create the post
    post = Post(
        title=title,
        description=description,
        slug=slug,
        image_url=image_url,
        url=url
    )
    db.session.add(post)
    db.session.commit()

    return jsonify({
        'id': post.id,
        'title': post.title,
        'description': post.description,
        'slug': post.slug,
        'image_url': post.image_url,
        'url': post.url
    }), 201
