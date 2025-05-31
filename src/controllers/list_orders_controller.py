from .interfaces.order_lister_interface import OrderListerInterface
from src.models.interfaces.orders_interface import OrderRepositoryInterface

class OrderListerController(OrderListerInterface):
  def __init__(self, repository: OrderRepositoryInterface)-> None:
    self.__repository = repository

  def list_orders(self, user_id)-> dict:
    orders = self.__repository.list_orders_by_user_id(user_id)
    return self.__format_response(user_id, orders)

  def __format_response(self, user_id:int, orders)->dict:
    return {
      "result":{
        "user_id": user_id,
        "orders": orders
      }
    }



