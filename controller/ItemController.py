from flask import request, render_template, redirect, session, Blueprint
from service.DBSessionStarter import db_session


bp = Blueprint('item_controller', __name__)  # Create a Blueprint named 'root'


# # add review to the item
# @bp.route('/shop/items/<int:item_id>/review', methods=['POST'])
# def post_shop_items_int_review(item_id):
#     json = request.get_json()
#     id = json['id']
#     item_id = json['item_id']
#     text = json['text']
#     rating = json['rating']
#     user_login = json['user_login']
#     write_database_data('feedback', [id, item_id, text, rating, user_login])
#     return 'feedback added'
#
#
# # watch all reviews of the item
# @bp.route('/shop/items/<int:item_id>/review', methods=['GET'])
# def get_shop_items_int_review(item_id):
#     return get_database_data('feedback', ['id', 'item_id', 'text', 'rating', 'user_login'], f"id = '{item_id}'")
#
#
# # watch review of the item
# @bp.route('/shop/items/<int:item_id>/review/<int:review_id>', methods=['GET'])
# def get_shop_items_int_review_int(item_id, review_id):
#     return get_database_data('feedback', ['id', 'item_id', 'text', 'rating', 'user_login'])
#
#
# # change review of the item
# @bp.route('/shop/items/<int:item_id>/review/<int:review_id>', methods=['PUT'])
# def put_shop_items_int_review_int(item_id, review_id):
#     json = request.get_json()
#     id = json['id']
#     item_id = json['item_id']
#     text = json['text']
#     rating = json['rating']
#     user_login = json['user_login']
#     update_database_data('feedback', {'id': id, 'item_id': item_id, 'text': text, 'rating': rating,
#                                       'user_login': user_login}, f"id = '{id}'")
#     return 'success'
