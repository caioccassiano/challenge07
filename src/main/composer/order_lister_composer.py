from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.orders.order_repository import OrderRepository
from src.controllers.list_orders_controller import OrderListerController
from src.view.order_lister_view import OrderListerView

def order_lister_composer():
  repository = OrderRepository(db_connection_handler)
  controller = OrderListerController(repository)
  view = OrderListerView(controller)
  return view
