from abc import ABC, abstractmethod

class OrderCreateInterface(ABC):
  
  @abstractmethod
  def create_order(self, description:str)->dict: pass

  