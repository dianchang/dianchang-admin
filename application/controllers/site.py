# coding: utf-8
from datetime import date, timedelta
from flask import render_template, Blueprint
from ..utils.permissions import UserPermission
from ..models.dc import db as dc_db, User as DCUser, Question as DCQuestion, Answer as DCAnswer

bp = Blueprint('site', __name__)


@bp.route('/')
@UserPermission()
def index():
    """Index page."""
    user_dates = []
    user_data = []
    for i in xrange(0, 7):
        target_date = date.today() - timedelta(days=i)
        users_count = DCUser.query.filter(dc_db.func.date(DCUser.created_at) == target_date).count()
        user_dates.insert(0, '%d.%d' % (target_date.month, target_date.day))
        user_data.insert(0, users_count)

    question_dates = []
    question_data = []
    for i in xrange(0, 7):
        target_date = date.today() - timedelta(days=i)
        questions_count = DCQuestion.query.filter(dc_db.func.date(DCQuestion.created_at) == target_date).count()
        question_dates.insert(0, '%d.%d' % (target_date.month, target_date.day))
        question_data.insert(0, questions_count)

    answer_dates = []
    answer_data = []
    for i in xrange(0, 7):
        target_date = date.today() - timedelta(days=i)
        answers_count = DCAnswer.query.filter(dc_db.func.date(DCAnswer.created_at) == target_date).count()
        answer_dates.insert(0, '%d.%d' % (target_date.month, target_date.day))
        answer_data.insert(0, answers_count)
    return render_template('site/index.html', user_dates=user_dates, user_data=user_data,
                           question_dates=question_dates, question_data=question_data,
                           answer_dates=answer_dates, answer_data=answer_data)

# @bp.route('/about')
# def about():
#     """About page."""
#     return render_template('site/about.html')
