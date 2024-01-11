from flask import request, render_template, redirect, session, Blueprint
from entity.User import User
from service.DBSessionStarter import db_session
from repository.UserRepository import *

bp = Blueprint('auth_controller', __name__)  # Create a Blueprint named 'root'


@bp.route('/register', methods=['GET'])
def get_register():
    return render_template('register.html', login=session.get('login'), admin=session.get('admin'))


# register user
@bp.route('/register', methods=['POST'])
def post_register():
    name = request.form['name']
    surname = request.form['surname']
    password = request.form['password']
    phone_number = request.form['phone_number']
    login = request.form['login']
    user = User(name, surname, password, phone_number, login)
    save_new_user(user)
    session['login'] = login
    return redirect('/profile')


@bp.route('/logout', methods=['POST'])
def post_logout():
    del session['login']
    return redirect('/')


@bp.route('/login', methods=['GET'])
def get_login():
    return render_template('login.html', login=session.get('login'), admin=session.get('admin'))


# login user
@bp.route('/login', methods=['POST'])
def post_login():
    login = request.form['login']
    password = request.form['password']
    user = get_user_by_login(login)
    if user and len(user.name) > 0 and user.password == password:
        session['login'] = login
        return redirect('/profile')
    else:
        return render_template('login.html', error="Wrong password", login=session.get('login'),
                               admin=session.get('admin'))
