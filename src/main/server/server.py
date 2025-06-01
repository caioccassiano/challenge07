from flask import Flask
from src.models.settings.db_connection_handler import db_connection_handler
from src.main.routes.users_routes import user_routes_bp
from src.main.routes.orders_routes import order_routes_bp

db_connection_handler.connect_to_db()

app = Flask(__name__)

app.register_blueprint(user_routes_bp)
app.register_blueprint(order_routes_bp)




