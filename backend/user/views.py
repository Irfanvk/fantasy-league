from flask import Blueprint, render_template
from user.forms import RegisterForm
fantasy_app = Blueprint('fantasy_app', __name__)


@fantasy_app.route('/login')
def login():
    return "User login"

@fantasy_app.route('/register', methods('GET','POST'))
def register():
    form = RegisterForm()
    return render_template('',form=form)