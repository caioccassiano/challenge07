from .create_user_controller import CreateUserController

class MockUserRepository:
  def __init__(self)-> None:
    self.registry_user_atributes = {}

  def create_user(self, username, password):
    self.registry_user_atributes["username"] = username
    self.registry_user_atributes["password"] = password
    return {
      "id":1,
      "username":username
    }


def test_create_user():
  repository = MockUserRepository()
  controller = CreateUserController(repository)

  username = "rosicaio"
  password = "caio1002"

  response = controller.create_user(username, password)

  print()
  print(response)
  print(repository.registry_user_atributes)

  assert repository.registry_user_atributes["password"] != password
  assert repository.registry_user_atributes["username"] == username

  assert response["data"]["type"] == "User"


