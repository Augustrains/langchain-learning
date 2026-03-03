"""
Simple utility module for demo purposes.
Contains greeting, math utilities, and a simple data processor.
"""

import math


def hello_world():
    """Print a hello message."""
    print("Hello, World!")


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def factorial(n: int) -> int:
    """Compute factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


class DataProcessor:
    """
    A simple data processor class.
    Provides normalization and statistics.
    """

    def __init__(self, data):
        self.data = data

    def normalize(self):
        """Normalize data to range [0, 1]."""
        if not self.data:
            return []
        min_val = min(self.data)
        max_val = max(self.data)
        if max_val == min_val:
            return [0 for _ in self.data]
        return [(x - min_val) / (max_val - min_val) for x in self.data]

    def mean(self):
        """Return the mean of the data."""
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)


def compute_circle_area(radius: float) -> float:
    """Return area of a circle."""
    return math.pi * radius ** 2


if __name__ == "__main__":
    hello_world()
    print("2 + 3 =", add(2, 3))
    print("Factorial 5 =", factorial(5))

    processor = DataProcessor([10, 20, 30])
    print("Normalized:", processor.normalize())
    print("Mean:", processor.mean())