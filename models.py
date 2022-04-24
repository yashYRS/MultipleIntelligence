from flask_login import UserMixin
from __init__ import db


class User(UserMixin, db.Model):
    # primary keys are required by SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    game_sessions = db.relationship('GameSession', backref='user', lazy=True)

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.name = name
        self.email = email
        self.password = password


class GameSession(db.Model):
    # Store information about every game played by user
    session_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    games = db.relationship('SingleGame', backref='game_session', lazy=True)


class SingleGame(db.Model):
    gameid = db.Column(db.Integer, primary_key=True)

    category_name = db.Column(db.String(100))
    category_image_path = db.Column(db.String(100))
    game_name = db.Column(db.String(100))

    level = db.Column(db.Integer)
    score = db.Column(db.Float)
    session_id = db.Column(db.Integer, db.ForeignKey('game_session.session_id'), nullable=False)

    def __init__(self, category_name, game_name):
        category_images = {
            'Word': '/static/images/word.png',
            'Logic': '/static/images/Logic.png',
            'Self': '/static/images/Self.png',
            'People': '/static/images/People.png',
            'Picture': '/static/images/Picture.png',
            'Nature': '/static/images/Nature.png',
            'Music': '/static/images/Music.png',
            'Body': '/static/images/Body.png',
        }
        self.category_name = category_name
        self.category_image_path = category_images[category_name]
        self.game_name = game_name
