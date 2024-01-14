from typing import Sequence, Any, Callable


class Seq:
    """Represents a sequence."""

    def __init__(self, seq: Sequence[Any]):
        """
        Initialize the Seq object.

        Args:
            seq (Sequence[Any]): The sequence to be initialized.
        """
        self.seq = list(seq)

    def __str__(self):
        """
        Return a string representation of the Seq object.

        Returns:
            str: The string representation of the Seq object.
        """
        return str(self.seq)

    def map(self, func: Callable[[Any], Any]) -> "Seq":
        """
        Apply a mapping function to every element in the sequence.

        Args:
            func (Callable[[Any], Any]): The mapping function to be applied.

        Returns:
            Seq: A new Seq object with mapped elements.
        """
        new_seq = []

        for element in self.seq:
            new_seq.append(func(element))

        return Seq(new_seq)

    def filter(self, func: Callable[[Any], bool]) -> "Seq":
        """
        Filter the sequence based on a filtering function.

        Args:
            func (Callable[[Any], bool]): The filtering function to be applied.

        Returns:
            Seq: A new Seq object with filtered elements.
        """
        new_seq = []

        for element in self.seq:
            if func(element):
                new_seq.append(element)

        return Seq(new_seq)

    def take(self, number: int) -> "Seq":
        """
        Take the first `number` elements from the sequence.

        Args:
            number (int): The number of elements to take.

        Returns:
            Seq: A new Seq object with the first `number` elements.
        """
        return Seq(self.seq[:number])


if __name__ == '__main__':
    fibo = Seq([1, 1, 2, 3, 5, 8, 13, 21])

    mapped_seq = fibo.map(lambda x: x * 2 - 1)
    print('Mapped seq:', mapped_seq)

    cut_seq = fibo.take(5)
    print('Cut seq:', cut_seq)

    filtered_seq = fibo.filter(lambda x: x >= 5)
    print('Filtered Sequence:', filtered_seq)
