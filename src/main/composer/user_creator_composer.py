from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.users.users_repository import UserRepository
from src.controllers.create_user_controller import CreateUserController
from src.view.user_creator_view import UserCreatorView

def user_creator_composer():
  repository = UserRepository(db_connection_handler)
  controller = CreateUserController(repository)
  view = UserCreatorView(controller)
  return view


