from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler
class TagCreatorController:
    '''
        responsible for implementing the logic of creating a tag
    '''
    def create(self, product_code: str) -> Dict:
        '''
            create a tag
        '''
        path_from_tag = self.__create_tag(product_code)
        formatted_reponse = self.__format_reponse(path_from_tag)
        return formatted_reponse

    def __format_reponse(self, path_from_tag: str) -> Dict:
        '''
            format response
        '''
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{path_from_tag}.png'
            }
        }
    
    def __create_tag(self, product_code: str) -> str:
        '''
            create a tag
        '''
        barcode_handler = BarcodeHandler()
        path_from_tag = barcode_handler.create_barcode(product_code)
        return path_from_tag

