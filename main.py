class Color:
    """Represents a color."""

    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, r: int, g: int, b: int):
        """
        Initialize the Color object.

        Args:
            r (int): The red color component.
            g (int): The green color component.
            b (int): The blue color component.
        """
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        """
        Return a string representation of the Color object.

        Returns:
            str: The string representation of the Color object.
        """
        return (
            f'{Color.START};{self.r};'
            f'{self.g};{self.b}{Color.MOD}'
            f'●{Color.END}{'m'}'
        )

    def __eq__(self, other: "Color") -> bool:
        """
        Check if two Color objects are equal.

        Args:
            other (Color): The other Color object to compare with.

        Returns:
            bool: True if the Color objects are equal, False otherwise.
        """
        return (
                (self.r, self.g, self.b) ==
                (other.r, other.g, other.b)
        )

    def __add__(self, other: "Color") -> "Color":
        """
        Perform addition between two Color objects.

        Args:
            other (Color): The other Color object to add.

        Returns:
            Color: The resulting Color object after addition.
        """
        return Color(
            min(self.r + other.r, 255),
            min(self.g + other.g, 255),
            min(self.b + other.b, 255)
        )

    def __hash__(self):
        """
        Return the hash value of the Color object.

        Returns:
            int: The hash value of the Color object.
        """
        return hash((self.r, self.g, self.b))

    def __mul__(self, c: float) -> "Color":
        """
        Perform multiplication between a Color object and a scalar.

        Args:
            c (float): The scalar to multiply with.

        Returns:
            Color: The resulting Color object after multiplication.
        """
        cl = -256 * (1 - c)
        f = 259 * (cl + 255) / (255 * (259 - cl))

        return Color(
            min(int(f * (self.r - 128) + 128), 255),
            min(int(f * (self.g - 128) + 128), 255),
            min(int(f * (self.b - 128) + 128), 255),
        )


if __name__ == "__main__":
    blue = Color(0, 0, 255)
    red = Color(255, 0, 0)

    print(f'Blue point - {blue}')
    print(f'Pink point - {blue + red}')

    print(f'Is blue equal to red?  {blue == red}')

    print(f'Dim red - {red * 0.3}')