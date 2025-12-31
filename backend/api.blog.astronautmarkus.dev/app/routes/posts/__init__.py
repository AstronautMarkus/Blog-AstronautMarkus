from flask import Blueprint

public_posts_bp = Blueprint('public_posts', __name__)

from . import (get_posts, visit_post)