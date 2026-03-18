"""
test_utils.py - Tests for utils.py
Run with: python -m pytest test_utils.py
"""

import pytest
from utils import (
    reverse_string, is_palindrome, count_words,
    factorial, is_prime, fibonacci,
    flatten, remove_duplicates, chunk,
)


# ── String tests ─────────────────────────────────────────────────────────────

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False

def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("  one  ") == 1
    assert count_words("") == 0


# ── Math tests ────────────────────────────────────────────────────────────────

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(13) is True
    assert is_prime(1) is False
    assert is_prime(9) is False

def test_fibonacci():
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]


# ── List tests ────────────────────────────────────────────────────────────────

def test_flatten():
    assert flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert remove_duplicates([]) == []

def test_chunk():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    with pytest.raises(ValueError):
        chunk([1, 2, 3], 0)
