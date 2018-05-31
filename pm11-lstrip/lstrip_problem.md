I want you to write a function that accepts an iterable and an object and returns a new iterable with all items from the original iterable except any item at the beginning of the iterable which is equal to the object should be skipped.

Here's an example:
>>> lstrip([0, 0, 1, 0, 2, 3], 0)
[1, 0, 2, 3]
>>> lstrip('  hello ', ' ')
['h', 'e', 'l', 'l', 'o', ' ']

As a bonus, return an iterator (for example a generator) from your lstrip function instead of a list. ✔️
>>> x = lstrip([0, 1, 2, 3], 0)
>>> x
<generator object <genexpr> at 0x7f0b18b0fbf8>
>>> list(x)
[1, 2, 3]
>>> list(x)
[]

Here's another bonus to do after you've made your lstrip function return a lazy iterable: allow your lstrip function to accept a function as its second argument which will determine whether the item should be stripped. ✔️

The function will be executed with each item individually and as long as the function returns True the item should be removed from the beginning of the iterable.

For example:
>>> def is_falsey(value): return not bool(value)
>>> list(lstrip(['', 0, 1, 0, 2, 'h', ''], is_falsey))
[1, 0, 2, 'h', '']
>>> list(lstrip([-4, -2, 2, 4, -6], lambda n: n < 0))
[2, 4, -6]

Automated tests for this week's exercise can be found here. You'll need to write your function in a module named lstrip.py next to the test file. To run the tests you'll run "python test_lstrip.py" and check the output for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.
