from flask import request, render_template, redirect, session, Blueprint
from service.DBSessionStarter import db_session


bp = Blueprint('compare_controller', __name__)  # Create a Blueprint named 'root'

# # get comparison list
# # no database table for comparison
# @bp.route('/shop/compare/<int:cmp_id>', methods=['GET'])
# def get_compare(cmp_id):
#     return 'GET /shop/compare/<int:cmp_id>'
#
#
# # change comparison list
# # no database table for comparison
# @bp.route('/shop/compare/<int:cmp_id>', methods=['PUT'])
# def put_compare(cmp_id):
#     return 'PUT /shop/compare/<int:cmp_id>'
#
#
# # add item to comparison
# # no database table for comparison
# @bp.route('/shop/compare', methods=['POST'])
# def post_compare():
#     return 'POST /shop/compare'
