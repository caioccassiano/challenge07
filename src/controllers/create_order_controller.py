from .interfaces.order_create_interface import OrderCreateInterface
from src.models.interfaces.orders_interface import OrderRepositoryInterface


class OrderCreateController(OrderCreateInterface):
  def __init__(self, repository:OrderRepositoryInterface)-> None:
    self.__repository = repository

  def create_order(self, user_id:int, description:str):
    self.__validate_request(user_id, description)
    new_order = self.__insert_new_order(user_id, description)
    return self.__format_response(new_order=new_order)

    

  def __validate_request(self, user_id, description)-> None:
    if not user_id or not description:
      raise Exception("Invalid input data")
    
  def __insert_new_order(self, user_id, description)->None:
    new_order = self.__repository.insert_order(user_id, description)
    return new_order
  
  def __format_response(self, new_order)->dict:
    return {
      "new_order":{
        "status": "Accepted",
        "attribute": new_order
      }
    }
  



