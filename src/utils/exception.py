class CustomException(Exception):
    """
    Custom exception class to wrap around exceptions for better logging.
    """
    def __init__(self, message, original_exception=None):
        super().__init__(message)
        self.original_exception = original_exception
