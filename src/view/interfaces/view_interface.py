from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from abc import ABC, abstractmethod

class ViewInterface(ABC):

  @abstractmethod
  def handle(self, http_request: HttpRequest)-> HttpResponse: pass


  