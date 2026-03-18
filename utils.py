"""
utils.py - A collection of simple Python utility functions.
"""


# ── String utilities ────────────────────────────────────────────────────────

def reverse_string(s: str) -> str:
    """Return the reverse of a string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (case-insensitive, ignores spaces)."""
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_words(s: str) -> int:
    """Return the number of words in a string."""
    return len(s.split())


# ── Math utilities ───────────────────────────────────────────────────────────

def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list[int]:
    """Return the first n Fibonacci numbers."""
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


# ── List utilities ───────────────────────────────────────────────────────────

def flatten(nested: list) -> list:
    """Flatten a nested list of arbitrary depth."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def remove_duplicates(lst: list) -> list:
    """Return a list with duplicates removed, preserving order."""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]


def chunk(lst: list, size: int) -> list[list]:
    """Split a list into chunks of a given size."""
    if size <= 0:
        raise ValueError("Chunk size must be greater than 0.")
    return [lst[i:i + size] for i in range(0, len(lst), size)]


# ── File utilities ───────────────────────────────────────────────────────────

def read_lines(filepath: str) -> list[str]:
    """Read a file and return its lines as a list (stripped of newlines)."""
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


def write_lines(filepath: str, lines: list[str]) -> None:
    """Write a list of strings to a file, one per line."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
