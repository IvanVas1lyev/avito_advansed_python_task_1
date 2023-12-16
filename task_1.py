import sys
from datetime import datetime


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


if __name__ == "__main__":
    original_write = sys.stdout.write
    sys.stdout.write = my_write

    print("1, 2, 3")

    sys.stdout.write = original_write
