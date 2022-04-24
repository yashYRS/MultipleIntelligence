from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app():
    # creates the Flask instance, __name__ is the name of the Python module
    app = Flask(__name__, template_folder='templates', static_url_path='/static')
    # it is used by Flask and extensions to keep data safe
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    # it is the path where the SQLite database file will be saved
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    # deactivate Flask-SQLAlchemy track modifications
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Initialiaze sqlite database
    db.init_app(app)

    # Create a Login Manager instance
    login_manager = LoginManager()
    # define the redirection path when login required and we attempt to access without being logged in
    login_manager.login_view = 'login'
    # configure it for login
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    # reload user object from the user ID stored in the session
    def load_user(user_id):
        # since the user_id is just the primary key of our user table
        # use it in the query for the user
        return User.query.get(int(user_id))

    # # blueprint for auth routes in our app
    # # blueprint allow you to orgnize your flask app
    # blueprint for non-auth parts of app
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
