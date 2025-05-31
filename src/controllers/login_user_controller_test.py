from .login_user_controller import LoginUserController
from src.drivers.passwort_handler import PasswordHandler

username = "miltonccassiano"
password = "milton123"
hashed_password = PasswordHandler().encrypt_password(password)


class MockRepository:
  def get_user_by_username(self, username):
    return (10, username, hashed_password)
  

def test_login():
  mock_repository = MockRepository()
  controller = LoginUserController(mock_repository)
  response = controller.login(username=username,password=password)

  assert response ["data"]["username"] == username
  assert response ["data"]["token"] is not None

  print()
  print(response)
  print(response["data"]["token"])
  print()
  print(response["data"]["username"])

  