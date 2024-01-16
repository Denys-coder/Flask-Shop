from flask import request, render_template, redirect, session, Blueprint
from service.DBSessionStarter import db_session

bp = Blueprint('favourite_controller', __name__)  # Create a Blueprint named 'root'

# # get all favourite items for specified list
# @bp.route('/shop/favourites/<int:list_id>', methods=['GET'])
# def get_favourites(list_id):
#     return get_database_data('wishlist', ['id', 'name', 'user_login', 'item_id'], f"list_id = '{list_id}'")
#
#
# # change favourite list
# @bp.route('/shop/favourites/<int:list_id>', methods=['PUT'])
# def put_favourites(list_id):
#     json = request.get_json()
#     id = json['id']
#     name = json['name']
#     user_login = json['user_login']
#     item_id = json['item_id']
#     update_database_data('wishlist', {'id': id, 'name': name, 'user_login': user_login, 'item_id': item_id},
#                          f"list_id = '{list_id}'")
#     return 'favourite list was updated'
