# PyMorsels My Takeaways

## [get_earliest](https://github.com/euccas/PyMorsels/tree/master/pm01-get_earliest)    (2/18/18)
- tuple unpacking (aka multiple assignment) is very powerful
- the ability to compare tuples is powerful

```python
def get_earliest(*dates):
    """Return earliest of given MM/DD/YYYY-formatted date strings."""
    def date_key(date):
        (m, d, y) = date.split('/')
        return (y, m, d)
    return min(dates, key=date_key)
```

## [count_words](https://github.com/euccas/PyMorsels/tree/master/pm02-count_words)   (2/25/18)
- from collection import defaultdict, defaultdict(int) sets default value 0
- from collection import defaultdict, Counter object counts how many times an element appears using dictionary
- remove punctuation in a sentence: notice the punctuation always appears after a letter (or before), so we can use strip() to remove them.
- re.findall()

```python
re.findall(pattern, string, flags=0)
```
Return all non-overlapping matches of pattern in string, as a list of strings

## [compact](https://github.com/euccas/PyMorsels/tree/master/pm03-compact)    (3/1/18)
- loop through a list, use i, item = enumerate to avoid using [index]
- zip(iter1, iter2) => [(iter1[0], iter2[0]), (iter1[1], iter2[1]), …, (iter1[n-1], iter2[n-1])]
- use * unpack a list
- object(), only equals to self, not any other objects
- A generator function is one way to make an iterator
- make a generator function by changing all our list appends into yield statements instead of returning a list

using * unpacking inside a list. This feature was added in Python 3.5. The * here is "unpacking" each of the items in our sequence into this new list, after object(). We're making object() the first item in our second list because a new object will not be compared as equal to any of the items in sequence (each object is only equal to itself by default).

## [negate](https://github.com/euccas/PyMorsels/tree/master/pm04-negate)   (3/14/18)
- list comprehension
- multi-dimentional list comprehension: use multi-line style to make it easier to read

```python
    return [
        [-n for n in row]
        for row in matrix
    ]
```

- Performance testing: my two solutions negate_0, negate_1. negate_0 iterates the list elements O(N), negate_1 uses list comprehension. negate_1 is faster.
- How to get negative number: ```-n``` is faster than ```-1 * n```
- [Talk on list comprehension](https://www.youtube.com/watch?v=5_cJIcgM7rw&__s=pftdsryd1xjaeaz5sgjo)
- [Read on list comprehension](http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/)

## [tail](https://github.com/euccas/PyMorsels/tree/master/pm05-tail) (3/19/18)
- The usage of ```-n``` to slice a list (iterable): ```nums[-3:]``` returns the last *three* elements, same as ```nums[len(nums)-3:]```
- Slice object can be used to remove repetitive code, such as slicing a list in multiple conditions with different index.
```python
if n == 1:
    index = slice(0, 1)
else:
    index = slice(-(n-1), None)
nums = nums[index]
```
- Deque: assign a maximum length of the deque, and deque will remove elements from head when keep appending elements when its full.
  - We're setting the maximum size of our deque to n. When you append to a deque which has reached it's maximum length, it will efficiently remove the item closest to the beginning before appending the new item. So this is an efficient way to keep track of the most recent n items we've seen.
  - Deque can be initialized with a iterable
- Convert any iterable to a list: list(iterable)
```python
str = "hello"
list(str) # ['h', 'e', 'l', 'l', 'o']
```
- List unpacking with * (since python 3.5)
```
for item in iterable:
    items = [*items[-(n-1):], item]
```
- [Introduction of Deque](https://pymotw.com/3/collections/deque.html?__s=pftdsryd1xjaeaz5sgjo)

## [is_anagram](https://github.com/euccas/PyMorsels/tree/master/pm06-is_anagram) (3/26/18)

## [circle](https://github.com/euccas/PyMorsels/tree/master/pm06-is_anagram) (4/2/18)
- Property decorators, setters and getters in Python
- __repr__, __str__ relies on __repr__ by default
- Python 3.6+, new f string: ```f'test({a})'```

## [multimax](https://github.com/euccas/PyMorsels/tree/master/pm08-multimax)  (4/15/18)
- Difference of "offline algorithm" and "online algorithm". Difference of processing a list and an iterable without known length.
- Key function, and the usage of key function in functions. Think key function as calculating scores of the original input data.
- Use lambda in function default argument. The lambda function will only be created once, and be referenced when the function is called multiple times.

## [uniques_only](https://github.com/euccas/PyMorsels/tree/master/pm09-uniques_only)  (5/6/18)
- Sets are unordered. It doesn't guarantee consistent order.
- Sets rely on hashes for lookups so containment checks won't slow down as our hash grows in size.
- Python 3.6+ feature: ```dict.fromkeys``` create a dictionary (which has unique keys that maintain insertion ordered as of Python 3.6)
```python
dict.fromkeys(iterable)
```
- Check for hashability: from collections.abc import Hashable
```python
if isinstance(item, Hashable): # is hashable
```
- "it's easier to practice forgiveness than permission". Use exception handling
```python
    for item in iterable:
        try:
            if item not in seen_hashable:
                yield item
                seen_hashable.add(item)
        except TypeError:
            if item not in seen_unhashable:
                yield item
                seen_unhashable.append(item)
```

## [group_by](https://github.com/euccas/PyMorsels/tree/master/pm10-group_by)  (5/30/18) 
- Use defaultdict, setdefault() whenever you have if/else to handle key exists/not case
- setdefault(): returns the dict[key] when key exists, otherwise returns the default value you set
- itertools groupby utility: works when the items to be grouped are all consecutive

```python
    iterable = sorted(iterable, key=key_func)
    for key, items in groupby(iterable, key=key_func):
        groups[key] = list(items)
    return groups
```
- Lambda function usage: in function argument, will be computed only once

```python
    if key_func is None:
        key_func = lambda x: x
```

```python
def group_by(iterable, key_func=lambda x: x):
```

- PEP8: never use lambda function to assign a value. Use def instead.

```python
    if key_func is None:
        def key_func(x): x
```

- Dictionary comprehension

```python
    return {
        key: list(items)
        for key, items in groupby(iterable, key=key_func)
    }
```

## [lstrip](https://github.com/euccas/PyMorsels/tree/master/pm11-lstrip)  (5/30/18)
- itertools dropoff function: dropoff(test_function, iterable). This function returns the original iterable while dropping off the items that make the test_function returns True.
- Skim the itertools documents, take a look at the many functions for working with iterables in a lazy and efficient fashion
- built-in function callable(): use it to decide whether a variable is a function
- iterater protocal: iter_val = iter(iterable), next(iter_val), exception StopIteration error
- try, except, else
