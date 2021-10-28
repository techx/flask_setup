import os
from flask import Flask, session, request

app = None
db = None


def create_app():
    global app, db, session
    app = Flask(__name__)

    @app.errorhandler(404)
    def page_not_found(err):
            return 'RIP 404', 404

    # register module blueprints
    from app.counter.views import counter_bp
    app.register_blueprint(counter_bp)

    return app
