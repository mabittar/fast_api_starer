class OptionalNumbersError(Exception):
    """Custom error raises when both optional numbers not be null"""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)

        
class EmailMustContainsAt(Exception):
    """Custom error raises when both optional numbers not be null"""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)
