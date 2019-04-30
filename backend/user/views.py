from flask import Blueprint

fantasy_app = Blueprint('fantasy_app', __name__)


@fantasy_app.route('/login')
def login():
    return "User login"
