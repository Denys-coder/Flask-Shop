from flask import redirect, Blueprint
from service.DBSessionStarter import db_session

bp = Blueprint('root_controller', __name__)  # Create a Blueprint named 'root'


@bp.route('/', methods=['GET'])
def get_home():
    return redirect('/about')
