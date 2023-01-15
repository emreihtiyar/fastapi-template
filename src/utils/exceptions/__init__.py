class InvalidJWTException(ValueError):
    """Exception raised for invalid JWT token.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = "Invalid JWT token"):
        self.message = message


class InvalidJWTSignatureException(ValueError):
    """Exception raised for invalid JWT token signature.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = "Invalid JWT token signature"):
        self.message = message