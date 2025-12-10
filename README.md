# HW22 – O(N) Python Solutions

## Task Definition

### Function `is_sum_two`

-   **Parameters:**
    -   `numbers` (list of integers)
    -   `sum` (integer)
-   **Returns:** `True` if any two numbers in the list sum up to `sum`, otherwise `False`.

**Examples:**

```py
is_sum_two([1, 2, 3, 4], 4)  # → True
is_sum_two([1, 2, 3, 4], 2)  # → False
```

### Function `max_negative_repr`

-   **Parameters:**
    -   `numbers` (list of integers)
-   **Returns:** The **largest positive number** in the list that has its negative counterpart present, or `-1` if none exists.

**Examples:**

```py
max_negative_repr([100, 4, 1, -1, -4, -100])  # → 100
max_negative_repr([100, 4, 1, 1, 4, 100, -1])  # → 1
max_negative_repr([100, 4, 1, 1, 4, 100, 1, -2])  # → -1
```

---

## 📝 Description

This project provides **linear-time solutions** to two classic problems using Python:

1. `is_sum_two`: finds if any two numbers in a list sum to a target value using a **hash set**.
2. `max_negative_repr`: finds the largest positive number with a negative counterpart in the list using **set-based lookup**.

The repository includes **unit tests**, proper **package structure**, and **VSCode configuration** for convenient development.

---

## 🎯 Purpose

-   Reinforce knowledge of **hash-based algorithms**
-   Handle **edge cases** such as duplicates, zeros, negatives, and empty lists
-   Write **clean, maintainable Python code**
-   Practice **unit testing** and automated validation

---

## 🔍 How It Works

### `is_sum_two`

1. Initialize an empty set `seen`.
2. For each number `x` in the list:
    - Check if `sum - x` exists in `seen`.
    - If yes → return `True`.
    - Otherwise, add `x` to `seen`.
3. Return `False` if no pair found.

**Time complexity:** O(N)  
**Space complexity:** O(N)

### `max_negative_repr`

1. Convert the list to a set `s` for **fast membership testing**.
2. Iterate through positive numbers in the list:
    - If `-num` exists in the set, track the maximum.
3. Return the maximum found, or `-1` if none exists.

**Time complexity:** O(N)  
**Space complexity:** O(N)

---

## 📜 Output Example

```py
from src import is_sum_two, max_negative_repr

# Example 1
print(is_sum_two([1, 2, 3, 4], 4))  # True

# Example 2
print(is_sum_two([1, 2, 3, 4], 10))  # False

# Example 3
print(max_negative_repr([100, 4, 1, -1, -4, -100]))  # 100

# Example 4
print(max_negative_repr([1, 2, 3]))  # -1
```

---

## 📦 Usage

-   Import the functions:

```py
from src import is_sum_two, max_negative_repr

numbers = [1, 2, 3, 4, -2]
target = 5

if is_sum_two(numbers, target):
    print("Found a pair with the target sum!")

max_num = max_negative_repr(numbers)
print(f"Largest number with negative counterpart: {max_num}")
```

---

## 🧪 Running Tests

All unit tests are in the `tests/` folder.  
To run the tests:

### Using `unittest` CLI

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### Using VSCode Test Explorer

-   Open VSCode
-   Install Python extension (if not installed)
-   Ensure `python.testing.unittestEnabled` is `true` in `.vscode/settings.json`
-   Run tests via **Test Explorer** (click "Run All Tests")

### Expected Output

```
TEST 1 PASSED
TEST 2 PASSED
...
TEST N PASSED
```

All tests include:

-   Basic and edge cases
-   Large numbers
-   Negative numbers and duplicates
-   Empty list and single-element lists

---

## ✅ Dependencies

-   Python 3.10+
-   Standard library only (`typing`, `unittest`)

---

## 🗂 Project Structure

```
HW22/
├─ .gitignore
├─ .vscode/
│  ├─ launch.json
│  ├─ settings.json
│  └─ tasks.json
├─ src/
│  ├─ __init__.py
│  ├─ is_sum_two.py
│  └─ max_negative_repr.py
└─ tests/
   ├─ __init__.py
   ├─ test_is_sum_two.py
   └─ test_max_negative_repr.py
```

---

## 📊 Project Status

**Status:** ✅ Completed  
All tests pass, and both algorithms run in **O(N)** time. Ready for use in production or as a study reference.

---

## 📄 License

MIT License

---

## 🧮 Conclusion

This project demonstrates:

-   Efficient linear-time algorithms for common array problems
-   Proper Python package structure
-   Unit testing and VSCode integration
-   Handling of edge cases and large numbers

---

Made with ❤️ and `Python` by **Sam-Shepsl Malikin** 🎓
