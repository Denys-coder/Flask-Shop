from flask import request, render_template, redirect, session, Blueprint
from service.DBSessionStarter import db_session

bp = Blueprint('waitlist_controller', __name__)  # Create a Blueprint named 'root'

# # get wait list orders
# @bp.route('/shop/waitlist', methods=['GET'])
# def get_waitlist():
#     user_login = request.args.get('user_login')
#     return get_database_data('waitlist', ['user_login', 'item_id'], f"user_login = '{user_login}'")
#
#
# # create new wait list
# @bp.route('/shop/waitlist', methods=['PUT'])
# def put_waitlist():
#     json = request.get_json()
#     user_login = json['user_login']
#     item_id = json['item_id']
#     write_database_data('waitlist', [user_login, item_id])
#     return 'new waitlist item was added'
