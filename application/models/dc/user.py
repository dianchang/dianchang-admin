# coding: utf-8
from datetime import datetime
from flask import current_app
from .._base import dc_db as db


class DCUser(db.Model):
    __tablename__ = 'user'
    __bind_key__ = 'dc'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    name_edit_count = db.Column(db.Integer)
    email = db.Column(db.String(100), unique=True)
    desc = db.Column(db.String(200))
    avatar = db.Column(db.String(200), default='default.png')
    url_token = db.Column(db.String(100))
    location = db.Column(db.String(100))
    organization = db.Column(db.String(100))
    position = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    @property
    def avatar_url(self):
        config = current_app.config
        dc_domain = config.get('DC_DOMAIN')
        return "%s/uploads/avatars/%s" % (dc_domain, self.avatar)

    @property
    def profile_url(self):
        config = current_app.config
        dc_domain = config.get('DC_DOMAIN')
        return "%s/people/%d" % (dc_domain, self.id)
