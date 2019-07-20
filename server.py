import os
from flask import Flask, render_template, request, flash, redirect, session
from flask_sqlalchemy import SQLAlchemy
from twilio.rest import Client
from jinja2 import StrictUndefined

# Your Account SID from twilio.com/console
account_sid = os.environ["ACCOUNT_SID"]
# Your Auth Token from twilio.com/console
auth_token  = os.environ["AUTH_TOKEN"]

client = Client(account_sid, auth_token)




app = Flask(__name__)
db = SQLAlchemy()


@app.route('/')
def hello_world():
    """Homepage."""

    return render_template("add_affirmation.html")



@app.route('/message', methods = ['GET','POST'])
def send_message():
    msg = request.form.get("user_affirmation", 0)
    if msg:
        message = client.messages.create(
        to="+15049136010", 
        from_="+15592068349",
        body=msg)

    return 'Message has been sent', 200

def connect_to_db(app, database_uri="postgresql:///sampledb"):
    """Connect the database to Flask app."""

    # Configure to use PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__=='__main__':
    #connect_to_db(app)
    app.run(host="0.0.0.0")