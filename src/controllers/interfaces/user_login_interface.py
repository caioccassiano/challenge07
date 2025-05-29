from abc import ABC, abstractmethod

class LoginUserInterface(ABC):
  def login(self, username:str, password:str)-> dict: pass
  
