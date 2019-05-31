#! python
#
# models.py
# The models file is where the applications data structures (and their
# relationships) are defined
from app import db


# Establishing the many-to-many relationship table
# This is not being created with an associated model because it is an auxiliary
# table only meant to hold foreign keys used for many-to-many associations
subs = db.Table(
    'subscribers', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('chan_id', db.Integer, db.ForeignKey('channel.id'))
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    subscriptions = db.relationship(
        'Channel',
        secondary=subs,
        back_populates='subscribers',
        lazy='dynamic'
    )

    def subscribe(self, chan):
        if not self.is_subscribed(chan):
            self.subscriptions.append(chan)

    def unsubscribe(self, chan):
        if self.is_subscribed(chan):
            self.subscriptions.remove(chan)

    def is_subscribed(self, chan):
        return chan in self.subscriptions

    def __repr__(self):
        return self.username


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    subscribers = db.relationship(
        'User',
        secondary=subs,
        back_populates='subscriptions',
        lazy='dynamic'
    )

    def __repr__(self):
        return self.name
