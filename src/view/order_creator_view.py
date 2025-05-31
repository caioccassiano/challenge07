from .interfaces.view_interface import ViewInterface
from src.controllers.interfaces.order_create_interface import OrderCreateInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse


class OrderCreateView(ViewInterface):
  def __init__(self, controller:OrderCreateInterface):
    self.__controller = controller


  def handle(self, http_request: HttpRequest)-> HttpResponse:
    user_id = http_request.params.get("user_id")
    order_description = http_request.body.get("description")
    headers_user_id = http_request.headers.get("uid")

    self.__validate_inputs(
      user_id=user_id, 
      description=order_description, 
      headers_user_id=headers_user_id)
    
    response = self.__controller.create_order(user_id, order_description)
    return HttpResponse(body= response, status_code=201 )


  
  def __validate_inputs(self, user_id:int, description:str, headers_user_id:any)->None:
    if(
      not user_id
      or not description
      or not isinstance(description,str)
      or int(headers_user_id) != int(user_id)
    ):
      raise Exception("Invalid Inputs")


