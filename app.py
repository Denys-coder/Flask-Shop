from flask import Flask, request
import sqlite3

app = Flask(__name__)


class DBReader:
    def __enter__(self):
        self.my_db = sqlite3.connect('identifier.sqlite')
        self.my_cursor = self.my_db.cursor()
        return self.my_cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.my_db.commit()
        self.my_db.close()


# register user
@app.route('/register', methods=['POST'])
def post_register():
    json = request.get_json()
    name = json['name']
    surname = json['surname']
    password = json['password']
    phone_number = json['phone_number']
    login = json['login']
    write_database_data('user', [name, surname, password, phone_number, login])
    return 'user registered'


# login user
@app.route('/login', methods=['POST'])
def post_login():
    json = request.get_json()
    login = json['login']
    password = json['password']
    user = get_database_data('user', [login, password])
    if password == user[1]:
        return 'user authenticated'
    else:
        return 'wrong password'


# watch item
@app.route('/shop/items/<int:item_id>', methods=['GET'])
def get_shop_items_int(item_id):
    return get_database_data('item', ['id', 'name', 'description', 'price', 'status', 'category'],
                             f"WHERE item_id = {item_id}")


# add review to the item
@app.route('/shop/items/<int:item_id>/review', methods=['POST'])
def post_shop_items_int_review(item_id):
    json = request.get_json()
    id = json['id']
    item_id = json['item_id']
    text = json['text']
    rating = json['rating']
    user_login = json['user_login']
    write_database_data('feedback', [id, item_id, text, rating, user_login])
    return 'feedback added'


# watch all reviews of the item
@app.route('/shop/items/<int:item_id>/review', methods=['GET'])
def get_shop_items_int_review(item_id):
    return get_database_data('feedback', ['id', 'item_id', 'text', 'rating', 'user_login'], f'WHERE id = {item_id}')


# watch review of the item
@app.route('/shop/items/<int:item_id>/review/<int:review_id>', methods=['GET'])
def get_shop_items_int_review_int(item_id, review_id):
    return get_database_data('feedback', ['id', 'item_id', 'text', 'rating', 'user_login'])


# change review of the item
@app.route('/shop/items/<int:item_id>/review/<int:review_id>', methods=['PUT'])
def put_shop_items_int_review_int(item_id, review_id):
    json = request.get_json()
    id = json['id']
    item_id = json['item_id']
    text = json['text']
    rating = json['rating']
    user_login = json['user_login']
    update_database_data('feedback', {'id': id, 'item_id': item_id, 'text': text, 'rating': rating,
                                      'user_login': user_login}, f"WHERE id = {id}")
    return 'success'


# get all items as user
@app.route('/shop/items', methods=['GET'])
def get_shop_items():
    category = request.args.get('category')
    order = request.args.get('order')
    price = request.args.get('price')
    page = request.args.get('page')
    return get_database_data('item', ['id', 'name', 'description', 'price', 'status', 'category'],
                             f"WHERE category = {category} AND order = {order} AND price = {price} AND page = {page}")


# search shop for items
@app.route('/shop/search', methods=['POST'])
def post_shop_search():
    json = request.get_json()
    input = json['input']
    return get_database_data('item', ['id', 'name', 'description', 'price', 'status', 'category'],
                             f"WHERE name LIKE '%{input}%'")


# get cart items
@app.route('/shop/cart', methods=['GET'])
def get_shop_cart():
    user_id = request.args.get('user_id')
    return get_database_data('cart', ['user_id', 'item_id', 'quantity'], f"WHERE user_id = {user_id}")


# add item to the cart
@app.route('/shop/cart', methods=['POST'])
def post_shop_cart():
    json = request.get_json()
    user_login = json['user_login']
    item_id = json['item_id']
    quantity = json['quantity']
    write_database_data('cart', [user_login, item_id, quantity])
    return 'item added to the cart'


# delete item from the cart
@app.route('/shop/cart/', methods=['DELETE'])
def delete_shop_cart():
    json = request.get_json()
    user_login = json['user_login']
    delete_database_data('cart', f'WHERE user_login = {user_login}')
    return 'item was deleted from the cart'


# get order data
@app.route('/shop/cart/order', methods=['GET'])
def get_shop_cart_order():
    user_login = request.args.get('user_login')
    return get_database_data('order', ['id', 'user_login', 'address', 'total_price', 'status'],
                             f"WHERE user_login = {user_login}")


# create new order
@app.route('/shop/cart/order', methods=['POST'])
def post_shop_cart_order():
    json = request.get_json()
    id = json['id']
    user_login = json['user_login']
    address = json['address']
    total_price = json['total_price']
    status = json['status']
    write_database_data('order', [id, user_login, address, total_price, status])
    return 'order added to the cart'


# get all favourite items for specified list
@app.route('/shop/favourites/<int:list_id>', methods=['GET'])
def get_favourites(list_id):
    return get_database_data('wishlist', ['id', 'name', 'user_login', 'item_id'], f"WHERE list_id = {list_id}")


# change favourite list
@app.route('/shop/favourites/<int:list_id>', methods=['PUT'])
def put_favourites(list_id):
    json = request.get_json()
    id = json['id']
    name = json['name']
    user_login = json['user_login']
    item_id = json['item_id']
    update_database_data('wishlist', {'id': id, 'name': name, 'user_login': user_login, 'item_id': item_id},
                         f"WHERE list_id = {list_id}")
    return 'favourite list was updated'


# get wait list orders
@app.route('/shop/waitlist', methods=['GET'])
def get_waitlist():
    user_login = request.args.get('user_login')
    return get_database_data('waitlist', ['user_login', 'item_id'], f"WHERE user_login = {user_login}")


# create new wait list
@app.route('/shop/waitlist', methods=['PUT'])
def put_waitlist():
    json = request.get_json()
    user_login = json['user_login']
    item_id = json['item_id']
    write_database_data('waitlist', [user_login, item_id])
    return 'new waitlist item was added'


# create new item
@app.route('/admin/items', methods=['POST'])
def post_admin_items():
    json = request.get_json()
    id = json['item_id']
    name = json['name']
    description = json['description']
    price = json['price']
    status = json['status']
    category = json['category']
    write_database_data('admin', [id, name, description, price, status, category])
    return 'new item was added'


# get all items as admin
@app.route('/admin/items', methods=['GET'])
def get_admin_items():
    category = request.args.get('category')
    order = request.args.get('order')
    price = request.args.get('price')
    page = request.args.get('page')
    return get_database_data('item', ['id', 'name', 'description', 'price', 'status', 'category'],
                             f"WHERE category = {category} AND order = {order} AND price = {price} AND page = {page}")


# get item as admin
@app.route('/admin/items/<int:items_id>', methods=['GET'])
def get_admin_items_int(item_id):
    return get_database_data('item', ['id', 'name', 'description', 'price', 'status', 'category'],
                             f"WHERE id = {item_id}")


# change item
@app.route('/admin/items/<int:items_id>', methods=['PUT'])
def put_admin_items():
    json = request.get_json()
    id = json['item_id']
    name = json['name']
    description = json['description']
    price = json['price']
    status = json['status']
    category = json['category']
    update_database_data('item', {'id': id, 'name': name, 'description': description, 'price': price, 'status': status,
                                  'category': category}, f"WHERE id = {id}")
    return 'item was updated'


# delete item
@app.route('/admin/items/<int:item_id>', methods=['DELETE'])
def delete_admin_items(item_id):
    delete_database_data('item', f"WHERE id = {item_id}")
    return 'item was deleted'


# get admin orders
@app.route('/admin/orders', methods=['GET'])
def get_admin_orders():
    return get_database_data('order', ['id', 'user_login', 'address', 'total_price', 'status'], "WHERE login = admin")


# create new order for admin
@app.route('/admin/orders', methods=['PUT'])
def put_admin_order():
    json = request.get_json()
    id = json['id']
    user_login = json['user_login']
    address = json['address']
    total_price = json['total_price']
    status = json['status']
    write_database_data('order', [id, user_login, address, total_price, status])
    return 'order added to the cart'


# get statistics for admin
@app.route('/admin/stats', methods=['GET'])
def get_admin_stats():
    return get_database_data('order', ['id', 'user_login', 'address', 'total_price', 'status'])


# change user data
@app.route('/user', methods=['PUT'])
def put_user(user):
    json = request.get_json()
    name = json['name']
    surname = json['surname']
    password = json['password']
    phone_number = json['phone_number']
    login = json['login']
    update_database_data('user', {'name': name, 'surname': surname, 'password': password, 'phone_number': phone_number,
                                  'login': login}, f"WHERE login = {login}")


# get comparison list
# no database table for comparison
@app.route('/shop/compare/<int:cmp_id>', methods=['GET'])
def get_compare(cmp_id):
    return 'GET /shop/compare/<int:cmp_id>'


# change comparison list
# no database table for comparison
@app.route('/shop/compare/<int:cmp_id>', methods=['PUT'])
def put_compare(cmp_id):
    return 'PUT /shop/compare/<int:cmp_id>'


# add item to comparison
# no database table for comparison
@app.route('/shop/compare', methods=['POST'])
def post_compare():
    return 'POST /shop/compare'


def get_database_data(table_name: str, columns: list, where: str = None):
    with DBReader() as cursor:
        if where is None:
            cursor.execute(f"SELECT {', '.join(columns)} FROM {table_name}")
        else:
            cursor.execute(f"SELECT {', '.join(columns)} FROM {table_name} WHERE {where}")
        data = cursor.fetchall()
    return data


def write_database_data(table_name: str, values: list):
    with DBReader() as cursor:
        quoted_values = [f"'{value}'" for value in values]
        cursor.execute(f"INSERT INTO {table_name} VALUES ({', '.join(quoted_values)})")


def update_database_data(table_name: str, key_value_pairs: dict, where: str):
    with DBReader() as cursor:
        wrapped_dict = {k: "'" + str(v) + "'" for k, v in key_value_pairs.items()}
        result_string = ', '.join([f'{key} = {value}' for key, value in wrapped_dict.items()])
        cursor.execute(f"UPDATE {table_name} SET {result_string} WHERE {where}")


def delete_database_data(table_name: str, where: str):
    with DBReader() as cursor:
        cursor.execute(f"DELETE FROM {table_name} WHERE {where}")


if __name__ == '__main__':
    app.run()
