# coding: utf-8
from flask import Blueprint, render_template, request
from ..utils.permissions import UserPermission
from ..models.dc import db as dc_db, User as DCUser

bp = Blueprint('user', __name__)


@bp.route('/user')
@UserPermission()
def index():
    page = request.args.get('page', 1, int)
    users = DCUser.query.paginate(page, 20)
    return render_template('user/index.html', users=users)
