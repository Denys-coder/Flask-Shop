from flask import request, render_template, redirect, session, Blueprint

from repository import UserRepository, CompareListRepository
from service.DBSessionStarter import db_session

bp = Blueprint('compare_controller', __name__)  # Create a Blueprint named 'root'


# get comparison list
@bp.route('/compare', methods=['GET'])
def get_compare():
    user = UserRepository.get_user_by_login(session['login'])
    user_comparable_categories = CompareListRepository.get_comparable_item_categories_by_user(user)
    return render_template('compare-select-category.html', user_comparable_categories=user_comparable_categories,
                           login=session.get('login'), admin=session.get('admin'))


# add item to comparison
@bp.route('/compare/<int:item_id>', methods=['POST'])
def post_compare(item_id):
    CompareListRepository.add_comparable_item(session['login'], item_id)
    return redirect('/catalog')


# compare items by category
@bp.route('/compare/<string:item_category>', methods=['GET'])
def get_comparable_items_by_category(item_category):
    comparable_items = CompareListRepository.get_comparable_items_by_category_by_user(item_category, session['login'])
    return render_template('compare-items.html', comparable_items=comparable_items, login=session['login'],
                           admin=session.get('admin'))
