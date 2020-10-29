import os
from flask import Flask, session, request
from flask_sqlalchemy import SQLAlchemy

app = None
db = None
bcrypt = None
migrate = None 


def load_from_env(app, *args):
    for a in args:
        app.config[a] = os.environ[a]

def create_app():
    global app, db, bcrypt, session, migrate
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
    
    # Database Setup (uncomment after database set in SQLALCHEMY_DATABASE_URI)
    #load database
    db = SQLAlchemy(app)
    from app.models import Item
    db.create_all()


    # register module blueprints
    from app.module1.views import module1_bp
    from app.module2.views import module2_bp
    app.register_blueprint(module1_bp)
    app.register_blueprint(module2_bp)


    # initialize db values 
    # initialize_db()
    
    """
    # Bonus Flask libraries, for more complex apps

    from flask_cors import CORS
    from flask_jwt_extended import JWTManager
    from flask_bcrypt import Bcrypt
    from flask_migrate import Migrate

    # configure database migrations
    migrate = Migrate()
    migrate.init_app(app, db)
    
    # configure CORS support
    CORS(app)   

    # configure Bcrypt for password hashing
    bcrypt = Bcrypt(app)

    # configure JWT (Javascript Web Token) authentication 
    jwt = JWTManager(app)
    app.config['JWT_SECRET_KEY'] = app.config['FLASK_SECRET_KEY']

    """

    return app


def initialize_db():
    from app.models import Item
    if len(Item.query.all()) == 0:
        first_item = Item()
        db.session.add(first_item)
        db.session.commit()