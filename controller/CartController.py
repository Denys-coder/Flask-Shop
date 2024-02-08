import yagmail
from flask import request, render_template, redirect, session, Blueprint

from our_celery import send_email
from repository import CartRepository
from service.DBSessionStarter import db_session
from repository.CartRepository import *
from repository.ItemRepository import *
from entity.DBClasses import Cart
import json

bp = Blueprint('cart_controller', __name__)  # Create a Blueprint named 'root'


# get cart items
@bp.route('/cart', methods=['GET'])
def get_shop_cart():
    login: str = session.get('login')
    cart_entries: list = get_cart_by_user_login(login)
    quantities: list = [cart_entry.quantity for cart_entry in cart_entries]
    item_ids: list = [cart_entry.item_id for cart_entry in cart_entries]
    items = get_items_by_ids(item_ids)
    return render_template('cart.html', items=items, quantities=quantities, login=session.get('login'),
                           admin=session.get('admin'))


@bp.route('/cart/make-order', methods=['POST'])
def post_make_order():
    login: str = session.get('login')
    delete_cart_by_user_login(login)
    cart_entries = CartRepository.get_cart_items_and_quantities_by_user_login(login)
    item_dicts = []
    for item, quantity in cart_entries:
        item_dict = {
            "name": item.name,
            "description": item.description,
            "price": item.price,
            "category": item.category,
            "status": item.status
        }
        item_dicts.append(item_dict)
    send_email.send_successful_order_email.delay(item_dicts)
    return redirect('/catalog')


# add item to the cart
@bp.route('/cart', methods=['POST'])
def post_shop_cart():
    item_id: int = int(request.form['item-id'])
    login: str = session.get('login')
    cart = Cart(login, item_id, 1)
    save_cart(cart)
    return redirect('/catalog')


# delete item from the cart
@bp.route('/cart/delete', methods=['POST'])
def delete_shop_cart():
    item_id = request.form['item-id']
    login = session.get('login')
    delete_cart_by_user_login_and_item_id(login, item_id)
    return redirect('/cart')
