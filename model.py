"""Model and database functions for Affirmation App."""
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

db = SQLAlchemy()
##############################################################################
# Model definitions

class User(db.Model):
    """User of Affirmation website."""
    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(55), nullable=False)
    lname = db.Column(db.String(55), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.Binary(128), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    user_message = db.relationship('Message',
                                    foreign_keys='Message.user_id',
                                    backref='user', lazy='dynamic')

def __repr__(self):
    """Provide helpful representation when printed."""
    return f"<User user_id={self.user_id} email={self.email} >"


class Message(db.Model):
    """For user messaging system."""
    __tablename__= "messages"

    message_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    body = db.Column(db.String(200), nullable = False)
    scheduled_date = db.Column(db.String(10), nullable = False)
    scheduled_time = db.Column(db.String(20), nullable = False)
    sent = db.Column(db.Boolean, nullable=False, default=False)

def __repr__(self):
        return '<Message {}>'.format(self.body)


def connect_to_db(app, db_uri= 'postgres:///peptalk'):
    """Connect the database to our Flask app."""
    # Configure to use our database.

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)


def example_data(bcrypt):
    """Create example data for the test database."""
    user1 = User(fname="Positive",
                lname="Friend",
                username="positiveFriend",
                email="positivity@gmail.com",
                phone="555-555-5555")
    db.session.add(user1)

    user2 = User(fname="Negative",
                lname="Friend",
                username="negativeFriend",
                email="negativity@gmail.com",
                phone="555-555-5555")
    db.session.add(user2)

    db.session.commit()


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print("Connected to DB.")
