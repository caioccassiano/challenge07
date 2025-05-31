from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest
from src.main.composer.user_login_composer import user_login_composer
from src.main.composer.user_creator_composer import user_creator_composer
from src.main.middleware.auth_jwt import auth_jwt_verify

bank_routes_bp = Blueprint("bank_routes", __name__)

@bank_routes_bp("/users/create", methods = ["POST"])
def create_user():
  http_request = HttpRequest(body=request.json)
  http_response = user_creator_composer().handle(http_request=http_request)

  return jsonify(http_response.body), http_response.status_code


