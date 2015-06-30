# coding: utf-8
from flask import render_template, Blueprint
from ..utils.permissions import UserPermission

bp = Blueprint('site', __name__)


@bp.route('/')
@UserPermission()
def index():
    """Index page."""
    return render_template('site/index.html')

# @bp.route('/about')
# def about():
#     """About page."""
#     return render_template('site/about.html')
