from abc import ABC, abstractmethod

class OrderCreateInterface(ABC):
  
  @abstractmethod
  def create_order(self, user_id:int, description:str)->dict: pass

  