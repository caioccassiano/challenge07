from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest
from src.main.middleware.auth_jwt import auth_jwt_verify
from src.main.composer.order_creator_composer import order_creator_composer
from src.main.composer.order_lister_composer import order_lister_composer

order_routes_bp = Blueprint("order_routes", __name__)

@order_routes_bp.route("/order/create/<user_id>", methods = ["POST"])
def create_order(user_id):
  token_information = auth_jwt_verify()

  http_request = HttpRequest(body=request.get_json(),
                             params={"user_id": user_id},
                             token_infos=token_information,
                             headers=request.headers)
  http_response = order_creator_composer().handle(http_request)
  return jsonify(http_response.body), http_response.status_code


@order_routes_bp.route("/orders/<user_id>", methods = ["GET"])
def list_orders_user(user_id):
  token_information = auth_jwt_verify()
  http_request = HttpRequest(
                             params={"user_id": user_id},
                             token_infos=token_information,
                             headers=request.headers)
  http_response = order_lister_composer().handle(http_request)
  return jsonify(http_response.body), http_response.status_code






