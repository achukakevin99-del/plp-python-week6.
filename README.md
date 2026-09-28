# Week 6 Assignment - Error Handling

This assignment practices using `try` and `except` to handle errors and keep Python programs from crashing.

## Files

* `safe_tools.py` - Contains three safe functions for division, number conversion, and dictionary key lookup.
* `unbreakable.py` - Demonstrates handling invalid input and division-by-zero errors without crashing.
* `README.md` - Describes the assignment, files, and why an `if` check alone cannot catch invalid number input.

## Why can the `if` check not catch `abc` on its own?

An `if` statement can check a condition after Python has successfully received and processed a value, but `abc` cannot be converted into an integer using `int()`. The conversion raises a `ValueError`, so `try` and `except` are needed to catch the error and prevent the program from crashing.

## Expected Output for safe_tools.py

```text
5.0
Cannot divide by zero
42
Not a number
82
Field not found
```
