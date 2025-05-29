from abc import ABC, abstractmethod


class CreateUserInterface(ABC):
  def create_user(self, username:str, password:str)-> None:
    pass


