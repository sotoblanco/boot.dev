# List Comprehension

Lists are the most common data structure you will use in Python, especially when managing hero inventories, spellbooks, or lists of monsters.

`for` loops are one of those tools that once you learn, you will want to use everywhere. However, your next level as a developer is learning when to replace a traditional `for` loop with a **list comprehension** to make your code more elegant.

![List Comprehension Syntax Diagram](image/image2.png)

List comprehensions offer a concise and highly readable way to create new lists from existing ones. However, you shouldn't go crazy with them—many developers still prefer traditional `for` loops when dealing with complex rules or nested logic to keep the code easy to follow. The goal is to build your intuition so you can decide which approach is best for the task at hand.

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

Imagine you looted a dungeon chest and want to filter the items to extract only the healing potions.

### Traditional Loop Approach
```python
chest = ["healing potion", "mana potion", "iron sword", "healing potion", "empty bottle"]
healing_potions = []

for item in chest:
    if "healing" in item:
        healing_potions.append(item)

print(healing_potions)
# Output: ['healing potion', 'healing potion']
```

### List Comprehension Approach
```python
chest = ["healing potion", "mana potion", "iron sword", "healing potion", "empty bottle"]

healing_potions = [item for item in chest if "healing" in item]

print(healing_potions)
# Output: ['healing potion', 'healing potion']
```

Both approaches achieve the exact same outcome, but the list comprehension version is shorter, cleaner, and maps directly to the mental model of filtering a collection.

While list comprehensions are great for simple cases, you should use standard loops if the logic becomes too complex or has multiple nested conditions. Readability and clean code are always the priorities.

# Assignment

A local band of goblins has raided the village armory and left behind a messy pile of swords. Most of them are rusted butter knives with low power levels.

Complete the `find_powerful_swords` function. It takes a list of sword power levels (`inventory`) and should return a new list containing only the powerful swords:

- [ ] Use a list comprehension to filter the list.
- [ ] Only include swords with a power level strictly greater than 4.

## Tips

- The basic syntax for filtering with a list comprehension is:
  ```python
  [expression for item in iterable if condition]
  ```
- In this exercise, the condition is that the power level of the sword must be greater than 4.
