from src.controllers.interfaces.user_create_interface import CreateUserInterface
from src.drivers.passwort_handler import PasswordHandler
from src.models.interfaces.users_interfaces import UserRepositoryInterface
from src.models.entities.users import UserTable
class CreateUserController(CreateUserInterface):
  def __init__(self, repository: UserRepositoryInterface)->None:
    self.__repository = repository
    self.__password_handler = PasswordHandler()

  def create_user(self, username:str, password:str)-> dict:
    self.__validate_body(username, password)
    hashed_password = self.__create_hash_password(password)
    new_user = self.__registry_new_user(username, hashed_password)
    formatted_response = self.__format_response(new_user)
    return formatted_response


  def __validate_body(self, username:str, password:str):
    if not username or not password:
      raise Exception("Invalid input data")
    
  def __create_hash_password(self, password:str)-> str:
    hashed_password = self.__password_handler.encrypt_password(password)
    return hashed_password
  
  def __registry_new_user(self, username:str, hashed_password:str )->dict:
    new_user = self.__repository.create_user(username,hashed_password)
    return new_user

  def __format_response(self, new_user:UserTable)-> dict:
    return {
      "data": {
        "type": "User",
        "count":1,
        "attributes": new_user
      }
    }
    
    