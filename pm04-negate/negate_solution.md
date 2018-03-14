This function has to make a new list and that new list has to have more new lists inside it. And we're going to need to loop over our old list of lists while doing that.

The most obvious way to do this for new Python programmers is to start with an empty list (new_matrix), loop over the old matrix, and appending new rows as we go. To make the new rows we'll need to make another empty list (new_row) and loop over the old row to negate each element as we add it to the new row list.

That looks like this:

```python
def negate(matrix):
    """Return new 2-D matrix with each number negated."""
    new_matrix = []
    for row in matrix:
        new_row = []
        for n in row:
            new_row.append(-n)
        new_matrix.append(new_row)
    return new_matrix
```

If you've been doing Python for a little while you might spot a bit of code that we could rewrite here. We're making an new empty list, looping over an old list, and appending to the new list each time you loop like this:

```python
new_row = []
for n in row:
    new_row.append(-n)
```

Whenever you see code written like this, you could copy-paste this into a list comprehension. Like this:

```python
new_row = [-n for n in row]
```

Or even:

```python
new_row = [
    -n
    for n in row
]
```

So we could solve this problem like this:

```python
def negate(matrix):
    """Return new 2-D matrix with each number negated."""
    new_matrix = []
    for row in matrix:
        new_row = [
            -n
            for n in row
        ]
        new_matrix.append(new_row)
    return new_matrix
```

Or without a variable (and with the list comprehension compressed onto one line because this one is still fairly readable that way):

```python
def negate(matrix):
    """Return new 2-D matrix with each number negated."""
    new_matrix = []
    for row in matrix:
        new_matrix.append([-n for n in row])
    return new_matrix
```

If you're not yet familiar with how to identify where you can use a list comprehension, I recommend reading this article I wrote on list comprehensions.

Note that at this point we are still making a new empty list, looping over an old list, and appending repeatedly to our new list as we loop. We could make another list comprehension here:

```python
def negate(matrix):
    """Return new 2-D matrix with each number negated."""
    return [
        [-n for n in row]
        for row in matrix
    ]
```

This is interesting code we have here. We have a list comprehension to build up a new matrix and each of its elements will be a new row created as the result of another list comprehension inside it. The structure of our code shows that we're making a list of lists, which isn't the case with the nested for loop code we started with.

I would like to note here that list comprehensions inside of list comprehensions can sometimes be pretty hard to read. This is a trivial example and I think this comprehension-inside-a-comprehension solution is easier to understand than the loop-inside-a-loop solution we started with.

Even this trivial example could be made hard to read though. We could write this solution like this:

```python
def negate(matrix):
    """Return new 2-D matrix with each number negated."""
    return [[-n for n in row] for row in matrix]
```

I find this much less readable than the multi-line solution though. Whitespace can really improve readability. I tend to break my list comprehensions over multiple lines because it usually improves readability.

If you're not yet sold on using nested list comprehensions for this exercise or on the idea of using list comprehensions in general, I recommend watching this talk I gave on comprehensions.