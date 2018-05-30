This week I want you to make a function that takes an iterable and a key function and returns a dictionary of items grouped by the values returned by the given key function.

For example, let's say we have a list of numbers, and a function that checks their remainder when we divide them by three. 

>>> numbers = [1, 4, 5, 6, 8, 19, 34, 55]
>>> def mod3(n): return n % 3
...

If we call our function with this list and key function, we should get the numbers back in a dictionary of numbers tied to their remainders (0, 1, 2).
 
>>> group_by(numbers, key_func=mod3)
{0: [6], 1: [1, 4, 19, 34, 55], 2: [5, 8]}

As a bonus, create a default behavior of returning the value back in the case that no key function is given. ✔️

>>> group_by([1, 2, 1, 3, 2, 1])
{1: [1, 1, 1], 2: [2, 2], 3: [3]}

If you finish the exercise and the bonus, also consider whether there's something that could be helpful for solving this in Python's standard library. You don't necessarily need to return a dictionary for this one, but you do need to return a dictionary-like object for the tests to pass.

Automated tests for this week's exercise can be found here. You'll need to write your function in a module named group_by.py next to the test file. To run the tests you'll run "python test_group_by.py" and check the output for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.
