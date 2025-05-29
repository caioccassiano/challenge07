from .passwort_handler import PasswordHandler

password = "Caio123"

def test_hashed_password():
  password_handler = PasswordHandler()
  hashed_password = password_handler.encrypt_password(password=password)
  response = password_handler.check_password(password=password, hashed_password=hashed_password)
  print(response)