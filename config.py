import os

FLASK_SECRET_KEY="dis_super_secret_key"
DEBUG=True
base = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(base, 'app.db')