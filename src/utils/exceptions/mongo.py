"""
Exceptions for the mongo module.
"""

class DbNotFoundError(Exception):
    """
    Exception raised when a database is not found.
    """
    message = "Database not found"

    def __init__(self, message: str = message):
        self.message = message
    