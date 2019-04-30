from flask import Flask
from backend.user.views import fantasy_app
from flask_mongoengine import MongoEngine

db = MongoEngine()
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    db.init_app(app)
    app.register_blueprint(fantasy_app)
    return app
