# coding: utf-8
from datetime import datetime
from .._base import dc_db as db


class DCQuestion(db.Model):
    __tablename__ = 'question'
    __bind_key__ = 'dc'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
