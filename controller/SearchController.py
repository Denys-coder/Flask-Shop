from flask import request, render_template, redirect, session, Blueprint
from service.DBSessionStarter import db_session

bp = Blueprint('search_controller', __name__)  # Create a Blueprint named 'root'

# # search shop for items
# @bp.route('/shop/search', methods=['POST'])
# def post_shop_search():
#     json = request.get_json()
#     input = json['input']
#     return get_database_data('item', ['id', 'name', 'description', 'price', 'category', 'quantity'],
#                              f"name LIKE '%{input}%'")
