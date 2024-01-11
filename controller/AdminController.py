from flask import request, render_template, redirect, session, Blueprint
from service.DBSessionStarter import db_session

bp = Blueprint('admin_controller', __name__)  # Create a Blueprint named 'root'


# # create new item
# @bp.route('/admin/items', methods=['POST'])
# def post_admin_items():
#     json = request.get_json()
#     id = json['item_id']
#     name = json['name']
#     description = json['description']
#     price = json['price']
#     status = json['status']
#     category = json['category']
#     write_database_data('admin', [id, name, description, price, status, category])
#     return 'new item was added'
#
#
# # get all items as admin
# @bp.route('/admin/items', methods=['GET'])
# def get_admin_items():
#     category = request.args.get('category')
#     order = request.args.get('order')
#     price = request.args.get('price')
#     page = request.args.get('page')
#     return get_database_data('item', ['id', 'name', 'description', 'price', 'category', 'quantity'],
#                              f"category = '{category}' AND order = '{order}' AND price = '{price}' AND page = '{page}'")
#
#
# # get item as admin
# @bp.route('/admin/items/<int:items_id>', methods=['GET'])
# def get_admin_items_int(item_id):
#     return get_database_data('item', ['id', 'name', 'description', 'price', 'category', 'quantity'],
#                              f"id = '{item_id}")
#
#
# # change item
# @bp.route('/admin/items/<int:items_id>', methods=['PUT'])
# def put_admin_items():
#     json = request.get_json()
#     id = json['item_id']
#     name = json['name']
#     description = json['description']
#     price = json['price']
#     status = json['status']
#     category = json['category']
#     update_database_data('item', {'id': id, 'name': name, 'description': description, 'price': price,
#                                   'category': category, 'quantity': quantity}, f"id = '{id}'")
#     return 'item was updated'
#
#
# # delete item
# @bp.route('/admin/items/<int:item_id>', methods=['DELETE'])
# def delete_admin_items(item_id):
#     delete_database_data('item', f"id = '{item_id}'")
#     return 'item was deleted'
#
#
# # get admin orders
# @bp.route('/admin/orders', methods=['GET'])
# def get_admin_orders():
#     return get_database_data('order', ['id', 'user_login', 'address', 'total_price', 'status'], "login = admin")
#
#
# # create new order for admin
# @bp.route('/admin/orders', methods=['PUT'])
# def put_admin_order():
#     json = request.get_json()
#     id = json['id']
#     user_login = json['user_login']
#     address = json['address']
#     total_price = json['total_price']
#     status = json['status']
#     write_database_data('order', [id, user_login, address, total_price, status])
#     return 'order added to the cart'
#
#
# # get statistics for admin
# @bp.route('/admin/stats', methods=['GET'])
# def get_admin_stats():
#     return get_database_data('order', ['id', 'user_login', 'address', 'total_price', 'status'])