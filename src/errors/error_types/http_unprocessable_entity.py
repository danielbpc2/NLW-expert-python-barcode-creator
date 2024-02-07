class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str = "Unprocessable Entity"):
        super().__init__(message)
        self.message = message
        self.name = "UnprocessableEntity"
        self.status_code = 422
