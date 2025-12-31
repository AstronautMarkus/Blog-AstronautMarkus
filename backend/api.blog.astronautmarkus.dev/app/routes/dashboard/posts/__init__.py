from flask import Blueprint

posts_bp = Blueprint('posts', __name__)

from . import create_post, delete_post, edit_post, list_posts