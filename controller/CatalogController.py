from flask import request, render_template, redirect, session, Blueprint
from service.DBSessionStarter import db_session
from repository.ItemRepository import *

bp = Blueprint('catalog_controller', __name__)  # Create a Blueprint named 'root'


@bp.route('/catalog', methods=['GET'])
def get_shop_items():
    items = get_all_items()
    return render_template('catalog.html', items=items, login=session.get('login'),
                           admin=session.get('admin'))


# watch item
@bp.route('/catalog/<int:item_id>', methods=['GET'])
def get_shop_items_int(item_id):
    item = get_item_by_id(item_id)
    return render_template('item.html', item=item, login=session.get('login'),
                           admin=session.get('admin'))
