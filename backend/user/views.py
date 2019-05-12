from flask import Blueprint, render_template
from ..user import RegisterForm

fantasy_app = Blueprint('fantasy_app', __name__,url_prefix='/auth')

@fantasy_app.route('/')
def home():
    return "Helloo"

@fantasy_app.route('/login')
def login():
    return "User login"

@fantasy_app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    return render_template('',form=form)