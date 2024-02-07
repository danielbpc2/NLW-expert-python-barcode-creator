from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controller.tag_creator_controller import TagCreatorController
from src.validators.tag_creator_validator import tag_creator_validator

class TagCreatorView:
    '''
        responsability for interacting with http
    '''

    def __validate(self, body: str):
        '''validate tags'''
        tag_creator_validator(body)

    def __create_tag(self, product_code: str):
        '''create tag'''
        tag_creator_controller = TagCreatorController()
        formatted_response = tag_creator_controller.create(product_code)
        return formatted_response

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        '''
            validate and create a tag
        '''
        body = http_request.body
        self.__validate(body)
        product_code = body['product_code']

        formatted_reponse = self.__create_tag(product_code)

        return HttpResponse(status_code=200, body=formatted_reponse)
