from flask import render_template, session, Blueprint
from service.DBSessionStarter import db_session


bp = Blueprint('about_controller', __name__)  # Create a Blueprint named 'root'


@bp.route('/about', methods=['GET'])
def get_about():
    return render_template('about.html', login=session.get('login'), admin=session.get('admin'))
