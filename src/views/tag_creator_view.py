from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        responsability for interacting with http
    '''

    def validate(self, product_code: str):
        # validate
        print('validate', product_code)

    def create_tag(self, product_code: str):
        # create tag
        print('create', product_code)

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        '''
            validate and create a tag
        '''
        body = http_request.body
        product_code = body['product_code']

        self.validate(product_code)
        self.create_tag(product_code)
        return HttpResponse(status_code=200, body={"status": "ok"})
    
