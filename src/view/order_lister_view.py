from .interfaces.view_interface import ViewInterface
from src.controllers.interfaces.order_lister_interface import OrderListerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class OrderListerView(ViewInterface):
  def __init__(self, controller: OrderListerInterface):
    self.__controller = controller

  def handle(self, http_request: HttpRequest)-> HttpResponse:
    user_id = http_request.params["user_id"]
    headers_user_id = http_request.headers["uid"]

    self.__validate_inputs(user_id, headers_user_id)
    response = self.__controller.list_orders(user_id)
    return HttpResponse(body=response, status_code=200)
    
  
  def __validate_inputs(self, user_id, headers_user_id)-> None:
    if(
      not user_id
      or int(headers_user_id) != int(user_id)

    ): raise Exception("Invalid Input")

    