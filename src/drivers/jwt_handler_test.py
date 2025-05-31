from .jwt_handler import JwtHandler

def test_jwt_handler():
  jwt_handler = JwtHandler()
  body= {
    "email": "caio@gmail.com",
    "username": "caioccasiano",
    "senha": "kdfjewbicoepwd"
  }

  token = jwt_handler.create_token(body=body)
  token_information = jwt_handler.decode_jwt_token(token)

  assert token is not None
  assert isinstance(token, str)
  assert token_information["username"] == body["username"]

  print()
  print()
  print()
  print(token)
  print()
  print(token_information)


