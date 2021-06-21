from flask import current_app
from app import db


class Feedback(db.Model):
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, primary_key=True)
    rating = db.Column(db.Integer)
    feedback = db.Column(db.String(140))

    def __repr__(self):
        return '<User {}>'.format(self.username)