from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.users.users_repository import UserRepository
from src.controllers.login_user_controller import LoginUserController
from src.view.user_login_view import LoginUserView

def user_login_composer():
  repository = UserRepository(db_connection_handler)
  controller = LoginUserController(repository)
  view = LoginUserView(controller)
  return view



