from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest
from src.main.composer.user_login_composer import user_login_composer
from src.main.composer.user_creator_composer import user_creator_composer

user_routes_bp = Blueprint("user_routes", __name__)

@user_routes_bp.route("/users/create", methods = ["POST"])
def create_user():
  
  http_request = HttpRequest(body=request.json)
  http_response = user_creator_composer().handle(http_request=http_request)

  return jsonify(http_response.body), http_response.status_code


@user_routes_bp.route("/users/login", methods = ["POST"])
def login_user():
  http_request = HttpRequest(body=request.json)
  http_response = user_login_composer().handle(http_request)

  return jsonify(http_response.body), http_response.status_code

