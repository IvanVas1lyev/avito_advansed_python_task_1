import sys
from typing import Callable


def redirect_output(filepath: str):
    """
    Decorator that redirects the output of a function to a file.
    """
    class FileWrapper:
        """
        Wrapper class that redirects the output to a file.
        """
        def __init__(self, path: str):
            self.file = None
            self.path = path
            self.original_stdout = sys.stdout

        def __enter__(self):
            """
            Enter method called when entering a 'with' statement.
            """
            self.file = open(self.path, "w")
            sys.stdout = self.file

            return self

        def __exit__(self, ex_type, ex_value, traceback):
            """
            Exit method called when leaving a 'with' statement.
            """
            self.file.close()
            sys.stdout = self.original_stdout

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            """
            Wrapper function that redirects the function's output to a file.
            """
            with FileWrapper(filepath):
                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


@redirect_output("./function_output.txt")
def calculate():
    """
    Print matrix of powers of numbers from 1 to 19.
    """
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=" ")
        print()


if __name__ == "__main__":
    calculate()
