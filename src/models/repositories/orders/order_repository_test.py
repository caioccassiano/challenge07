from .order_repository import OrderRepository
from src.models.entities.users import UserTable
from src.models.settings.db_connection_handler import db_connection_handler
import pytest

db_connection_handler.connect_to_db()
@pytest.mark.skip(reason="tested")
def test_insert_order():
  user_id = 2
  description = "Limpar a casa"

  mock_connection = db_connection_handler
  repo = OrderRepository(mock_connection)
  repo.insert_order(user_id, description)


def test_list_orders_by_user_id():
  user_id = 2
  mock_connection = db_connection_handler
  repo = OrderRepository(mock_connection)
  response = repo.list_orders_by_user_id(user_id=user_id)
  print(response)
  for order in response:
    print(order.description)



