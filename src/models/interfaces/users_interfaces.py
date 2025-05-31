from abc import ABC, abstractmethod
from src.models.entities.users import UserTable
from typing import Optional

class UserRepositoryInterface(ABC):
  
  @abstractmethod
  def create_user(self, username:str, password:str)-> None:
    pass

  @abstractmethod
  def get_user_by_username(self, username:str)-> Optional[UserTable]:
    pass


