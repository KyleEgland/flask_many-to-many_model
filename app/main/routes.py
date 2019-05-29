#! python
#
# routes.py
# flask_many_to_many app main
from app import db
from app.main import bp
from app.models import User
from flask import jsonify
from flask import render_template
from flask import request


# @bp.before_app_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.last_seen = datetime.utcnow()
#         db.session.commit()
#     g.locale = str(get_locale())


@bp.route('/')
@bp.route('/index')
def index():
    # Render index
    return render_template('index.html')


@bp.route('/adduser', methods=['POST'])
def adduser():
    if request.get_json():
        content = request.get_json()

        user = User(username=content['username'])

        db.session.add(user)
        db.session.commit()

        return jsonify({'Status': 'Success!'})
    else:
        return jsonify({'ERR': 'There was no json found in body of request'})
