from abc import ABC, abstractmethod
from src.models.entities.orders import OrdersTable

class OrderRepositoryInterface(ABC):

  @abstractmethod
  def insert_order(self, user_id:int, description:str)-> None:
    pass

  @abstractmethod
  def list_orders_by_user_id(self, user_id:int)->list[OrdersTable]:
    pass

