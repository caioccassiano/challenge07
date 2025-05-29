from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
  def __init__(self)-> None:
    self.__conn_string = "sqlite:///projectstorage.db"
    self.__engine = None
    self.session = None

  def connect_to_db(self):
    self.__engine = create_engine(self.__conn_string)

  def get_engine(self):
    return self.__engine
  
  def __enter__(self):
    if self.__engine is None:
        self.connect_to_db()
    session_maker = sessionmaker(bind=self.__engine)
    self.session = session_maker()
    return self

  
  def __exit__(self, exc_type, exc_val, exc_tb):
    self.session.close()


  

db_connection_handler = DBConnectionHandler()

