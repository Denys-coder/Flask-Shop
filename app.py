from flask import Flask
from controller import AboutController
from controller import AdminController
from controller import AuthController
from controller import CartController
from controller import CatalogController
from controller import CompareController
from controller import FavouriteController
from controller import ItemController
from controller import OrderController
from controller import RootController
from controller import SearchController
from controller import UserController
from controller import WaitlistController
import config
import dto
import entity
import model
import properties
import service
import static
import service.DBSessionStarter

app = Flask(__name__)
app.secret_key = 'some_password'

app.register_blueprint(AboutController.bp)
app.register_blueprint(AdminController.bp)
app.register_blueprint(AuthController.bp)
app.register_blueprint(CartController.bp)
app.register_blueprint(CatalogController.bp)
app.register_blueprint(CompareController.bp)
app.register_blueprint(FavouriteController.bp)
app.register_blueprint(ItemController.bp)
app.register_blueprint(OrderController.bp)
app.register_blueprint(RootController.bp)
app.register_blueprint(SearchController.bp)
app.register_blueprint(UserController.bp)
app.register_blueprint(WaitlistController.bp)

if __name__ == '__main__':
    app.run()
