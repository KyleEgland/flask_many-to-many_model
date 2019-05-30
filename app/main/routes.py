#! python
#
# routes.py
# flask_many_to_many app main
from app import db
from app.main import bp
from app.models import Channel
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
    users = User.query
    channels = Channel.query
    # Render index
    return render_template('index.html', users=users, channels=channels)


@bp.route('/adduser', methods=['POST'])
def adduser():
    # Check the request for json
    if request.get_json():
        # If there is json in the request, assign it to the var content
        content = request.get_json()

        # Check for the existence of a user by the same name
        if User.query.filter_by(username=str(content['username'])).first():
            # Return an error if that username already exists
            return jsonify({'error': 'Username already exists'})

        # Should the name not already exist, create a user with that name
        user = User(username=str(content['username']))

        # Add the new user to the session
        db.session.add(user)

        # Commit the session
        db.session.commit()

        msg = "Added user: {}".format(user.username)

        # Return a resonse to the caller
        return jsonify({'status': msg})

    else:
        # Should there have been no json in the request, tell the caller
        return jsonify({'error': 'There was no json found in body of request'})


@bp.route('/addchannel', methods=['POST'])
def addchannel():
    # Check the request for json
    if request.get_json():
        # If there is json in the request, assign it to the var content
        content = request.get_json()

        # Check for the existence of a user by the same name
        if Channel.query.filter_by(name=str(content['channelname'])).first():
            # Return an error if that username already exists
            return jsonify({'error': 'Channel with that name already exists'})

        # Should the name not already exist, create a user with that name
        chan = Channel(name=str(content['channelname']))

        # Add the new user to the session
        db.session.add(chan)

        # Commit the session
        db.session.commit()

        msg = "Channel with name {} has been created".format(chan.name)

        # Return a resonse to the caller
        return jsonify({'status': msg})

    else:
        # Should there have been no json in the request, tell the caller
        return jsonify({'error': 'There was no json found in body of request'})
