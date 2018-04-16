This week you needed to make a function that takes an iterable and returns all maximum values found in the iterable.

One way to solve this problem is to loop through our iterable to find the maximum value and then loop through it again to find all values that are equal to it.

```python
def multimax(iterable):
    """Return a list of all maximum values."""
    max_item = None
    for item in iterable:
        if max_item is None or item > max_item:
            max_item = item
    items = []
    for item in iterable:
        if item == max_item:
            items.append(item)
    return items
```

This passes our tests, but there's a better way to go about finding our maximum value.

Python has a **built-in max function** that can be used for identifying the maximum value in an iterable:

```python
def multimax(iterable):
    """Return a list of all maximum values."""
    max_item = max(iterable)
    items = []
    for item in iterable:
        if item == max_item:
            items.append(item)
    return items
```

That's a lot shorter!

You might notice we can make this code even shorter by using a **list comprehension**. The way we can tell that a list comprehension is possible here is that our code has a new empty list (items), a for loop, an if statement, and an append to add items to the new list that started out as empty. We can copy-paste our way from a loop to a list comprehsion like this:

```python
def multimax(iterable):
    """Return a list of all maximum values."""
    max_item = max(iterable)
    return [
        item
        for item in iterable
        if item == max_item
    ]
```

So we have a couple different solutions that pass our tests. Let's take a look at the first bonus now.
 
## Bonus #1

For the first bonus, we were supposed to make sure our function returned an empty list when given an empty iterable.

Our first solution actually already passed this test. Here's a variation of our first solution that uses a comprehension:

```python
def multimax(iterable):
    """Return a list of all maximum values."""
    max_item = None
    for item in iterable:
        if max_item is None or item > max_item:
            max_item = item
    return [
        item
        for item in iterable
        if item == max_item
    ]
```

While that passes our tests, our shorter solutions that use the built-in max function fail them:

```
>>> multimax([])
Traceback (most recent call last):
  File "multimax.py", line 5, in multimax
ValueError: max() arg is an empty sequence
```

We could handle empty iterables by **catching the ValueError** that max raises:

```python
def multimax(iterable):
    """Return a list of all maximum values."""
    try:
        max_item = max(iterable)
    except ValueError:
        return []
    return [
        item
        for item in iterable
        if item == max_item
    ]
```

But if we look at the documentation for max, we'll see that it only raises a ValueError if no default value is specified. We could default the maximum value to None to ensure that an exception isn't raised for empty iterables:

```python
def multimax(iterable):
    """Return a list of all maximum values."""
    max_item = max(iterable, default=None)
    return [
        item
        for item in iterable
        if item == max_item
    ]
```

This might seem inefficient because we loop through the iterable even when there is no max. It isn't though, because there will only be no maximum value if the iterable is empty and if it's empty then we'll immediately get an empty list from that list comprehension (because there's simply nothing to loop over).

Okay let's talk about the second bonus now.
 
## Bonus #2
For the second bonus we were supposed to make sure our function worked for lazy iterables, like generators.

Our current solutions fail this requirement because they loop through our iterable twice and **generators can only be looped over one time only**.

We could keep track of the maximum values as we loop and manually build up a list of maximums:

```python
def multimax(iterable):
    """Return a list of all maximum values."""
    maximums = []
    for item in iterable:
        if not maximums or maximums[0] == item:
            maximums.append(item)
        elif item > maximums[0]:
            maximums = [item]
    return maximums
```

Since we're only looping over the given iterable once here, this should always work.

Or we could make a new list out of the given iterable and then find the max and loop over it again just as we did before:

```python
def multimax(iterable):
    """Return a list of all maximum values."""
    iterable = list(iterable)
    max_item = max(iterable, default=None)
    return [
        item
        for item in iterable
        if item == max_item
    ]
```

This isn't a good answer though because we're creating a copy of our whole iterable as a list just so we can loop over it twice and then discard it. This isn't very memory efficient. So I very much prefer the solution just before this one.

Okay let's take a look at the third bonus.
 
## Bonus #3

For the third bonus we were supposed to accept a key argument which is a function that will determine how our values should be compared to each other. **You can think of the key function as creating a "score" for each of our items.** We could store a list of items and their scores, find the maximum score, and then return all items with that score:

```python
def multimax(iterable, key=None):
    """Return a list of all maximum values."""
    if key is None:
        def key(item): return item
    item_scores = [
        (key(item), item)
        for item in iterable
    ]
    try:
        max_key = max(score for score, _ in item_scores)
    except ValueError:
        return []
    return [
        item
        for score, item in item_scores
        if score == max_key
    ]
```

Notice that we have a new "key" argument that defaults to None. If it's specified as None, we set the key variable to a function that accepts an item and returns the same item (which makes our function behave just like it did before when no key was specified).

This works, but again we're storing a list just to loop over it once.

Instead, let's solve this one the long way... by looping over all the items and keeping track of the current maximum key and the current maximum items list and then updating the key and the list as we find new maximums:

```python
def multimax(iterable, key=None):
    """Return a list of all maximum values."""
    if key is None:
        def key(item): return item
    max_key = None
    maximums = []
    for item in iterable:
        k = key(item)
        if k == max_key:
            maximums.append(item)
        elif not maximums or k > max_key:
            maximums = [item]
            max_key = k
    return maximums
```

Unfortunately we can't turn this into a list comprehension because we're sometimes appending and sometimes clearing our list and starting over.

The last thing we could do to improve this is to set the default value for our "key" argument to a function instead of None:

```python
​def multimax(iterable, key=lambda x: x):
    """Return a list of all maximum values."""
    max_key = None
    maximums = []
    for item in iterable:
        k = key(item)
        if k == max_key:
            maximums.append(item)
        elif not maximums or k > max_key:
            maximums = [item]
            max_key = k
    return maximums
```

Note that this doesn't define a new function every time we call multimax, but only defines the function once and uses that function reference as the default whenever a key isn't specified while calling multimax.

Also note that this lambda expression looks to be assigned to a variable (as PEP8 recommends against) but we're using it as the default value for an argument in our function and there's no way to use def to define a function in this case without making a second variable to then reference as the default.

I don't use lambda expressions often, but this is one of those cases where I might use one in my own code.
