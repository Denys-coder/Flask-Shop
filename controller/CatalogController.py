from flask import request, render_template, redirect, session, Blueprint
from service.DBSessionStarter import db_session
from repository.ItemRepository import *

bp = Blueprint('catalog_controller', __name__)  # Create a Blueprint named 'root'


@bp.route('/catalog', methods=['GET'])
def get_shop_items():
    name = request.args.get('name')
    status = request.args.get('status')
    category = request.args.get('category')
    min_price = request.args.get('min-price')
    max_price = request.args.get('max-price')
    items = get_filtered_items(name, status, category, min_price, max_price)
    return render_template('catalog.html', name=name, status=status, category=category, min_price=min_price,
                           max_price=max_price, items=items, login=session.get('login'), admin=session.get('admin'))


# watch item
@bp.route('/catalog/<int:item_id>', methods=['GET'])
def get_shop_items_int(item_id):
    item = get_item_by_id(item_id)
    return render_template('item.html', item=item, login=session.get('login'),
                           admin=session.get('admin'))
