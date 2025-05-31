from .users_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler
from src.models.entities.users import UserTable
import pytest


db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Tested")
def test_create_user():
  username = "caioccassiano"
  password = "Caio123"

  mock_connection = db_connection_handler
  repo = UserRepository(mock_connection)
  response = repo.create_user(username, password)
  print(response)

def test_get_user_by_username():
  user_id = 2
  mock_connection = db_connection_handler
  repo = UserRepository(mock_connection)
  response = repo.get_user_by_username(user_id)
  print(response)
  print()
  print(response.username)
  



