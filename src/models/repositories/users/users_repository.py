from src.models.interfaces.users_interfaces import UserRepositoryInterface
from src.models.entities.users import UserTable

class UserRepository(UserRepositoryInterface):
  def __init__(self, db_connection)-> None:
    self.__db_connection = db_connection

  def create_user(self, username, password)-> None:
    with self.__db_connection as db:
      try: 
        user = UserTable(
          username = username,
          password = password
        )
        db.session.add(user)
        db.session.commit()
      except Exception as exception:
        db.session.rollback()
        raise exception
      
  def get_user_by_username(self, username):
    with self.__db_connection as db:
      try:
        user = (
          db.session
          .query(UserTable)
          .filter(UserTable.username == username)
          
        ).first()
        return user
      except Exception:
        return None
      





    