If you assume the input to compact is a list, a string, or another sequence (indexed from 0 upward), you could use indexes to check whether the current item is the same as the item before it:

```python
def compact(sequence):
    """Return new iterable with adjacent duplicate values removed."""
    deduped = []
    for i, item in enumerate(sequence):
        if i == 0 or item != sequence[i-1]:
            deduped.append(item)
    return deduped
```

We're always appending item 0 and then only appending subsequent items if they are not equal to the item just before their index.

Another way you could solve this is to zip together the original sequence with itself shifted by one so that the each item can compare itself with the one before:

```python
def compact(sequence):
    """Return new iterable with adjacent duplicate values removed."""
    deduped = []
    for item, previous in zip(sequence, [object(), *sequence]):
        if item != previous:
            deduped.append(item)
    return deduped
```

Note that we're using * unpacking inside a list. This feature was added in Python 3.5. The * here is "unpacking" each of the items in our sequence into this new list, after object(). We're making object() the first item in our second list because a new object will not be compared as equal to any of the items in sequence (each object is only equal to itself by default).

This solution is weird and maybe a little too clever. I think I prefer the index-based solution more than this one, even though I love using the zip function.

Let's take a look at the first bonus.

So our first bonus requires that we accept any iterable, not just sequences. Our first two solutions don't work with any iterable. The first one only works with iterables that can be indexed from 0 upward (like lists, tuples, strings, and other sequences). Our second solution doesn't work with lazy iterables (which will be consumed immediately after the * operator loops over our iterable, so the zip results will be empty).

This solution only loops over our iterable once, so it should work with all iterables:

```python
def compact(iterable):
    """Return new iterable with adjacent duplicate values removed."""
    deduped = []
    previous = None
    for item in iterable:
        if item != previous:
            deduped.append(item)
            previous = item
    return deduped
```

This doesn't pass our tests though! This doesn't work because if our list starts with None values, we've got a problem because previous starts at None so it'll look like the first value from our iterable should be removed.

We could fix this by setting a variable to keep track of whether we're at the beginning of our iterable:

```python
def compact(iterable):
    """Return new iterable with adjacent duplicate values removed."""
    deduped = []
    first = True
    for item in iterable:
        if first or item != previous:
            deduped.append(item)
            previous = item
            first = False
    return deduped
```

This "first" variable is True only at the very beginning, ensuring that we always add the first item instead of checking a "previous" variable.

We could also take the approach of setting our "previous" variable to a value that is only every equal to itself (like the object() thing we used before):

```python
def compact(iterable):
    """Return new iterable with adjacent duplicate values removed."""
    deduped = []
    previous = object()
    for item in iterable:
        if item != previous:
            deduped.append(item)
            previous = item
    return deduped
```

This is nice because we don't have to both check for "first" and compare each item to the previous one each time we loop.

Okay let's look at the second bonus.

For the second bonus we're supposed to return an iterator. A generator function is one way to make an iterator.

We can make a generator function by changing all our list appends into yield statements instead of returning a list:

```python
def compact(iterable):
    """Return new iterable with adjacent duplicate values removed."""
    previous = object()
    for item in iterable:
        if item != previous:
            yield item
            previous = item
```

Generator functions work in a fundamentally different way from regular functions in Python. You might want to check them out if you've never heard of them before.