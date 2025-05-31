from abc import ABC, abstractmethod

class OrderListerInterface(ABC):

  @abstractmethod
  def list_orders(self, user_id:int)->list :pass

