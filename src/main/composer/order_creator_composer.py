from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.orders.order_repository import OrderRepository
from src.controllers.create_order_controller import OrderCreateController
from src.view.order_creator_view import OrderCreateView

def order_creator_composer():
  repository = OrderRepository(db_connection_handler)
  controller = OrderCreateController(repository)
  view = OrderCreateView(controller)
  return view

