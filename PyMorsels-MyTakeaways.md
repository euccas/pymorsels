# PyMorsels My Takeaways

## get_earliest    (2/18/18)
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

## count_words    (2/25/18)
- from collection import defaultdict, defaultdict(int) sets default value 0
- from collection import defaultdict, Counter object counts how many times an element appears using dictionary
- remove punctuation in a sentence: notice the punctuation always appears after a letter (or before), so we can use strip() to remove them.
- re.findall()

```python
re.findall(pattern, string, flags=0)
```
Return all non-overlapping matches of pattern in string, as a list of strings

## compact    (3/1/18)
- loop through a list, use i, item = enumerate to avoid using [index]
- zip(iter1, iter2) => [(iter1[0], iter2[0]), (iter1[1], iter2[1]), …, (iter1[n-1], iter2[n-1])]
- use * unpack a list
- object(), only equals to self, not any other objects
- A generator function is one way to make an iterator
- make a generator function by changing all our list appends into yield statements instead of returning a list

using * unpacking inside a list. This feature was added in Python 3.5. The * here is "unpacking" each of the items in our sequence into this new list, after object(). We're making object() the first item in our second list because a new object will not be compared as equal to any of the items in sequence (each object is only equal to itself by default).

## negate   (3/14/18)
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