from abc import ABC, abstractmethod

class OrderListerController(ABC):

  @abstractmethod
  def list_orders(self, user_id:int)->list :pass

