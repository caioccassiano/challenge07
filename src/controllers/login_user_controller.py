from .interfaces.user_login_interface import LoginUserInterface
from src.models.repositories.users.users_repository import UserRepository
from src.models.interfaces.users_interfaces import UserRepositoryInterface
from src.drivers.jwt_handler import JwtHandler
from src.drivers.passwort_handler import PasswordHandler

class LoginUserController(LoginUserInterface):
  def __init__(self, repository:UserRepositoryInterface)-> None:
    self.__repository = repository
    self.__jwt_handler = JwtHandler()
    self.__password_handler = PasswordHandler()

  def login(self, username, password)-> dict:
    self.__validate_body(username, password)
    user = self.__find_user(username=username)
    user_id = user.id
    hashed_password = user.password
    self.__validate_password(password, hashed_password)
    token = self.__create_access_token(user_id=user_id)
    return self.__format_response(username, token)



  def __validate_body(self, username:str, password:str)->None:
    if not username or not password:
      raise Exception("Invalid input data!")
    
  def __find_user(self, username:str)-> dict:
    user = self.__repository.get_user_by_username(username)
    if not user:
      raise Exception("User does not exist")
    return user
  
  def __validate_password(self, password:str, hashed_password:str)->None:
    is_password_correct = self.__password_handler.check_password(password, hashed_password)
    if is_password_correct == None: raise Exception("Password is not valid")

  def __create_access_token(self, user_id)->str:
    payload = {"user_id": user_id}
    token = self.__jwt_handler.create_token(payload)
    return token
  
  def __format_response(self, username:str, token:str)->dict:
    return {
      "data":{
        "username": username,
        "token": token
      }
    }
  





  