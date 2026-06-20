# List Comprehension

Lists are the most common data structure you will use in Python due to their versatility and the wide variety of ways they can be manipulated.

List comprehensions build on this by offering a concise and highly readable way to create new lists from existing ones.

## The Syntax

A list comprehension consists of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The basic structure looks like this:

```python
new_list = [expression for item in iterable if condition]
```

Here is how the components map to a traditional loop:
1. **`expression`**: The value that gets added to the new list (often the item itself, or a modified version of it).
2. **`item`**: The variable representing the current element in the loop.
3. **`iterable`**: The sequence or collection you are looping through.
4. **`if condition`** (optional): A filter to determine whether the item should be included in the new list.

## Traditional Loop vs List Comprehension

Consider this example where we want to filter a list of fruits to only include those that contain the letter "a".

### Traditional Loop Approach
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for fruit in fruits:
    if "a" in fruit:
        new_list.append(fruit)

print(new_list)
# Output: ['apple', 'banana', 'mango']
```

### List Comprehension Approach
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

new_list = [fruit for fruit in fruits if "a" in fruit]

print(new_list)
# Output: ['apple', 'banana', 'mango']
```

Both approaches achieve the exact same outcome, but the list comprehension version is shorter, cleaner, and maps directly to the mental model of filtering a collection.

While list comprehensions are great for simple cases, you should use standard loops if the logic becomes too complex or has multiple nested conditions. Readability is always the priority.

# Assignment

In `main.py`, you will find a function called `find_powerful_sword` that filters a list of sword power levels using a traditional `for` loop.

Your task is to refactor this function to use a single-line list comprehension instead.

## Input

- `inventory`: A list of integers representing the power levels of swords in a player's inventory.

## Output

- A new list containing only the power levels that are strictly greater than 4.
