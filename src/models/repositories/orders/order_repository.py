from src.models.entities.orders import OrdersTable
from src.models.interfaces.orders_interface import OrderRepositoryInterface


class OrderRepository(OrderRepositoryInterface):

  def __init__(self, db_connection)-> None:
    self.__db_connection = db_connection
    

  def insert_order(self, user_id:int, description:str)-> None:
    with self.__db_connection as db:
      try:
        order = OrdersTable(
          user_id = user_id,
          description = description
        )
        db.session.add(order)
        db.session.commit()

      except Exception as exception:
        db.session.rollback()
        raise exception


  def list_orders_by_user_id(self, user_id:int)-> list[OrdersTable]:
    with self.__db_connection as db:
      try:
        orders = db.session.query(OrdersTable).filter(OrdersTable.user_id == user_id).all()
        return orders
      except Exception:
        return [] 


    