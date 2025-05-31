from .create_order_controller import OrderCreateController

class MockRepository:
  def __init__(self):
    self.received_data = {}
  
  def insert_order(self, user_id, descritpion):
    self.received_data={
      "id": 1,
      "user_id": user_id,
      "description":descritpion
    }
    return self.received_data
  
  
def test_create_order():
  mock_repository = MockRepository()
  controller = OrderCreateController(mock_repository)

  user_id = 1
  description = "Fazer compras"
  response = controller.create_order(user_id, description)
  
  print(response)

  assert response["new_order"]["status"] == "Accepted"
  assert "attribute" in response["new_order"]

  