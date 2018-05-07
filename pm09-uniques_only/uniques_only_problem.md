I want you to write a function that accepts an iterable and returns a new iterable with all items from the original iterable except for duplicates.

Here's an example:

```
>>> uniques_only([1, 2, 2, 1, 1, 3, 2, 1])
[1, 2, 3]
>>> nums = [1, -3, 2, 3, -1]
>>> squares = (n**2 for n in nums)
>>> uniques_only(squares)
[1, 9, 4]
```

As a bonus, return **an iterator** (for example a generator) from your uniques_only function instead of a list. This should allow your uniques_only function to accept infinitely long iterables (or other lazy iterables).

Here's another bonus to do after you've made your uniques_only function return a lazy iterable: allow your uniques_only function to work with **unhashable objects**.

For example when two lists with equal items are provided, they should be seen as duplicates:

```
>>> list(uniques_only([['a', 'b'], ['a', 'c'], ['a', 'b']]))
[['a', 'b'], ['a', 'c']]
```

For an extra bonus, make sure your function works efficiently with hashable items while still accepting **unhashable items**. This one is a little harder to test. There's an automated test (included below) that attempts to performance test your function.
