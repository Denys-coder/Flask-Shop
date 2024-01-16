from flask import request, render_template, redirect, session, Blueprint
from service.DBSessionStarter import db_session

bp = Blueprint('order_controller', __name__)  # Create a Blueprint named 'root'

# # get order data
# @bp.route('/shop/cart/order', methods=['GET'])
# def get_shop_cart_order():
#     user_login = request.args.get('user_login')
#     return get_database_data('order', ['id', 'user_login', 'address', 'total_price', 'status'],
#                              f"user_login = '{user_login}'")
#
#
# # create new order
# @bp.route('/shop/cart/order', methods=['POST'])
# def post_shop_cart_order():
#     json = request.get_json()
#     id = json['id']
#     user_login = json['user_login']
#     address = json['address']
#     total_price = json['total_price']
#     status = json['status']
#     write_database_data('order', [id, user_login, address, total_price, status])
#     return 'order added to the cart'
