from flask import request
from src.drivers.jwt_handler import JwtHandler

def auth_jwt_verify():
  jwt_handler = JwtHandler()
  raw_token = request.headers.get("Authorization")
  user_id = request.headers("uid")

  if not raw_token or not user_id:
    raise Exception("Invalid Auth informations")
  
  token = raw_token.split()[1] #We gotta do this because it's a Bearer token and tje [0] is gonna be "Bearer"
  token_informations = jwt_handler.decode_jwt_token(token) # We call the function to decode the token after extract it from raw_token
  token_uid = token_informations["user_id"] # We take the user_id so we can pass it as a parameter

  if user_id and token_uid and (int(token_uid)== int(user_id)):
    return token_informations
  
  raise Exception("User Unauthorized")
                           

  