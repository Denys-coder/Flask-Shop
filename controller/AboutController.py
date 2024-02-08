import yagmail
from flask import render_template, session, Blueprint

from repository import CartRepository
from properties.mail import *

import smtplib
from email.mime.text import MIMEText

bp = Blueprint('about_controller', __name__)  # Create a Blueprint named 'root'


@bp.route('/about', methods=['GET'])
def get_about():
    return render_template('about.html', login=session.get('login'), admin=session.get('admin'))
