# Class for error handling
class ErrorHandler:
    def handle_error(self, func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Error: {e}")
                return [], [], [], []  # return empty lists

        return wrapper