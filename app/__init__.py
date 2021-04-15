import os
from flask import Flask, session, request
from flask_sqlalchemy import SQLAlchemy

app = None
db = None


def load_from_env(app, *args):
    for a in args:
        app.config[a] = os.environ[a]

def create_app():
    global app, db, session
    app = Flask(__name__)


    # load config vars from file or environment
    if os.path.exists("config.py"):
        app.config.from_pyfile("../config.py")
        print("Loading secret configs from file")
    else:
        load_from_env(app, 'FLASK_SECRET_KEY',
                                    'DEBUG',
                                    'SQLALCHEMY_DATABASE_URI') 
        print("Loading secret configs from env")

    # register module blueprints
    from app.module1.views import module1_bp
    from app.module2.views import module2_bp
    app.register_blueprint(module1_bp)
    app.register_blueprint(module2_bp)

    """
    # Database Setup (uncomment after database set in SQLALCHEMY_DATABASE_URI)
    #load database
    db = SQLAlchemy(app)
    from app.models import Item

    db.create_all()
    """

    return app
