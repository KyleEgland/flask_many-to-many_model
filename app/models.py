#! python
#
# models.py
# The models file is where the applications data structures (and their
# relationships) are defined
from app import db


# Establishing the many-to-many relationship table
# This is not being created with an associated model because it is an auxiliary
# table only meant to hold foreign keys used for many-to-many associations
subscribers = db.Table(
    'subscribers',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('chan_id', db.Integer, db.ForeignKey('channel.id'))
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    subscriptions = db.relationship(
        'Channel',
        secondary=subscribers,
        backref=db.backref('subscribers', lazy='dynamic')
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __repr__(self):
        return '<Post {}>'.format(self.body)
