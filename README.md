# PythonExercises
## ex00 
### Truple
- **Ordered collections of elements:** Tuples store elements in a specific order, similar to lists.
- **Immutable:** Once created, you cannot modify the elements within a tuple.
- **Enclosed in parentheses ():** Elements are separated by commas.
- **Useful for:** Representing data that shouldn't be changed (e.g., coordinates, configuration values).
 ```python
fruits = ("apple", "banana", "orange")
print(fruits[1])   # Output: banana (access by index)

# Trying to modify an element will result in an error:
fruits[0] = "mango"  # TypeError: 'tuple' object does not support item assignment

```
### Set
- **Unordered collections of unique elements:** Sets don't guarantee the order in which elements are stored.
- **Duplicate elements are not allowed:** If you try to add a duplicate, it will be ignored.
- **Enclosed in curly braces {}:** Elements are separated by commas.
- **Useful for:** Checking membership, removing duplicates, performing set operations (union, intersection, difference).
 
 ```python
 unique_letters = {"a", "b", "c", "b"}  # "b" will be ignored
print(len(unique_letters))  # Output: 3 (only unique elements counted)

# Checking membership:
if "c" in unique_letters:
  print("c is present")
```
### Dictionary
- **Unordered collections of key-value pairs:** Unlike lists and sets, dictionaries associate a value with a unique key.
- **Keys must be immutable:** This ensures efficient retrieval based on the key. Strings, numbers, or tuples are commonly used as keys.
- **Values can be of any data type:** They can be numbers, strings, lists, other dictionaries, etc.
- **Enclosed in curly braces {}:** Keys and values are separated by colons (:), with key-value pairs separated by commas.
- **Useful for:** Storing data where you need to access it by a unique identifier (e.g., phonebook, configurations).
```python
person = {"name": "Alice", "age": 30, "hobbies": ["reading", "hiking"]}
print(person["name"])  # Output: Alice (access by key)

# Modifying values is allowed:
person["age"] = 31
print(person)  # Output: {'name': 'Alice', 'age': 31, 'hobbies': ['reading', 'hiking']}

  ```

## ex01
The `format()` function in Python is used to format a specified value into a specified format. In the provided code, `format(seconds_from_epoch, ',.4f')` is used to format the number of seconds since the epoch. The ',' option adds a comma as a thousand separator, and '.4f' specifies that the number should be a floating-point number with 4 digits after the decimal point. 
```python
 print(seconds_from_epoch)                    1712534417.322682
 print(format(seconds_from_epoch, ',.4f'))    1,712,534,417.3227
```

Scientific notation is a way of expressing numbers that are too large or too small to be conveniently written in decimal form. It is commonly used by scientists, mathematicians, and engineers. In the provided code, scientific notation is calculated in two ways:

-  Using Python's built-in formatting: `{seconds_from_epoch:.2e}`. The '.2e' format specifier is used to represent the number in scientific notation with 2 digits after the decimal point.

- Manually calculating the mantissa and exponent: The mantissa is calculated by normalizing the number to be between 1 and 10, and the exponent is calculated as the power of 10 needed to reach the original number from the mantissa. The `math.floor()` and `math.log10()` functions are used to calculate the exponent, and the mantissa is calculated by dividing the original number by 10 raised to the power of the exponent. The mantissa is then rounded to 2 decimal places using the `round()` function.
