class CatchException(Exception):
    def __init__(self, message: str, status_code: int = 400, response=None):
        self.status_code = status_code
        self.message = message
        self.response = response
        super().__init__(message)
