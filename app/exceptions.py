class AppError(Exception):
    """Base class for exceptions in this application."""
    
    def __init__(self, message):
        super().__init__(message)
