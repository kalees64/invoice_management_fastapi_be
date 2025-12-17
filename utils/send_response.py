class SendResponse(dict):
    def __init__(self, message: str, status_code: int = 200, response=None):
        super().__init__(
            statusCode=status_code,
            message=message,
            response=response
        )
