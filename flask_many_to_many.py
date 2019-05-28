#! python
# flask_many_to_many.py
# This file is what creates the Flask application.
from app import create_app
from app import db
from app.models import User
from app.models import Channel

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Channel': Channel}
