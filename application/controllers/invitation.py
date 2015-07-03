# coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import gen_salt
from ..utils.permissions import UserPermission
from ..models.dc import db as dc_db, InvitationCode as DCInvitationCode

bp = Blueprint('invitation', __name__)


@bp.route('/invitation')
@UserPermission()
def index():
    page = request.args.get('page', 1, int)
    codes = DCInvitationCode.query.order_by(DCInvitationCode.created_at.desc()).paginate(page, 20)
    return render_template('invitation/index.html', codes=codes)


@bp.route('/invitation/generate_codes')
@UserPermission()
def generate_codes():
    """生成邀请码"""
    for i in xrange(0, 5):
        hash_value = ''
        while True:
            hash_value = gen_salt(6)
            code = DCInvitationCode.query.filter(DCInvitationCode.code == hash_value).first()
            if not code:
                break
        code = DCInvitationCode(code=hash_value)
        dc_db.session.add(code)
        dc_db.session.commit()
    return redirect(url_for('.index'))
