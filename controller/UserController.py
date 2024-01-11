from flask import request, render_template, redirect, session, Blueprint

from entity.User import User
from service.DBSessionStarter import db_session
from repository.UserRepository import *

bp = Blueprint('user_controller', __name__)  # Create a Blueprint named 'root'


@bp.route('/profile', methods=['GET'])
def get_user():
    login = session['login']
    user = get_user_by_login(login)
    return render_template('profile.html', user=user, login=session.get('login'),
                           admin=session.get('admin'))


@bp.route('/profile/update', methods=['GET'])
def get_profile_update():
    login = session['login']
    user = get_user_by_login(login)
    return render_template('update-profile.html', user=user, login=session.get('login'),
                           admin=session.get('admin'))


# change user data
@bp.route('/profile', methods=['POST'])
def post_user():
    name = request.form['name']
    surname = request.form['surname']
    password = request.form['password']
    phone_number = request.form['phone_number']
    user = User(name, surname, password, phone_number, session['login'])
    update_user(user)
    return redirect('/profile')
