import sys
from datetime import datetime
from typing import Callable


def timed_output(func: Callable):
    """
    Decorator for the func.
    """
    original_write = sys.stdout.write

    def my_write(string_text: str):
        """
        Modifies how print() works by adding the current time
        to the beginning of the output.
        """
        now = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]: ")

        if string_text.startswith("\n"):
            original_write(string_text)
        else:
            original_write(now + string_text)

    def wrapper(*args, **kwargs):
        """
        Wrapper for the func.
        """
        sys.stdout.write = my_write
        func(*args, **kwargs)
        sys.stdout.write = original_write

    return wrapper


@timed_output
def print_greeting(name: str):
    """
    A function that greets the passed object.
    """
    print(f"Hello, {name}!")


if __name__ == "__main__":
    print_greeting("Nikita")
