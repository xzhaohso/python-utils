# python-utils 🐍

A collection of simple, well-tested Python utility functions.

## Functions

### 🔤 String
| Function | Description |
|---|---|
| `reverse_string(s)` | Reverse a string |
| `is_palindrome(s)` | Check if a string is a palindrome |
| `count_words(s)` | Count words in a string |

### 🔢 Math
| Function | Description |
|---|---|
| `factorial(n)` | Compute factorial of n |
| `is_prime(n)` | Check if n is prime |
| `fibonacci(n)` | Return first n Fibonacci numbers |

### 📋 List
| Function | Description |
|---|---|
| `flatten(nested)` | Flatten a nested list |
| `remove_duplicates(lst)` | Remove duplicates preserving order |
| `chunk(lst, size)` | Split list into chunks |

### 📁 File
| Function | Description |
|---|---|
| `read_lines(filepath)` | Read file lines into a list |
| `write_lines(filepath, lines)` | Write list of strings to a file |

## Usage

```python
from utils import fibonacci, is_palindrome, flatten

print(fibonacci(8))        # [0, 1, 1, 2, 3, 5, 8, 13]
print(is_palindrome("racecar"))  # True
print(flatten([1, [2, [3]]]))    # [1, 2, 3]
```

## Tests

```bash
pip install pytest
python -m pytest test_utils.py -v
```

## License

MIT
