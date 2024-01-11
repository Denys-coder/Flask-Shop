from flask import request, render_template, redirect, session, Blueprint
from service.DBSessionStarter import db_session
from repository.CartRepository import *
from repository.ItemRepository import *

bp = Blueprint('cart_controller', __name__)  # Create a Blueprint named 'root'


# get cart items
@bp.route('/cart', methods=['GET'])
def get_shop_cart():
    login: str = session.get('login')
    cart_entries: list = get_cart_by_user_login(login)
    quantities: list = [cart_entry.quantity for cart_entry in cart_entries]
    item_ids: list = [cart_entry.item_id for cart_entry in cart_entries]
    # item_ids_string = ", ".join(["'" + str(item_id) + "'" for item_id in item_ids])
    items = get_items_by_ids(item_ids)
    return render_template('cart.html', items=items, quantities=quantities, login=session.get('login'),
                           admin=session.get('admin'))


@bp.route('/cart/make-order', methods=['POST'])
def post_make_order():
    login: str = session.get('login')
    delete_cart_by_user_login(login)
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
