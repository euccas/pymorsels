We can test whether two words are anagrams by checking whether they have the same letters.

You might think to convert the words to sets to check whether they have the same letters:

```python
def is_anagram(word1, word2):
    """Return True if the given words are anagrams."""
    return set(word1) == set(word2)
```

That won't work for words that have the same letters but they occur a different number of times.

If we pass "sinks" into it we'll get {'s', 'i', 'n', ' k'} which doesn't account for how the number of occurrences of each letter. If we used a dictionary instead of a set, we could use the values to keep track of the number of times each character occurs.

Instead of set, we could make a function that accepts a string and returns a dictionary of character counts for the string:

```python
def count_letters(word):
    letters = {}
    for char in word:
        letters.setdefault(char, 0)
        letters[char] += 1
    return letters
```

Then we could use that instead of set in our is_anagram function:

```python
def is_anagram(word1, word2):
    """Return True if the given words are anagrams."""
    return count_letters(word1) == count_letters(word2)
```

That count_letters function might seem a little familiar. We solved a similar "count the number of times you see each thing" problem when we solved count_words.

You may remember from solving count_words that Python has a dictionary-like data structure in the standard library specifically meant for counting occurrences of things, collections.Counter:
from collections import Counter

```python
def is_anagram(word1, word2):
    """Return True if the given words are anagrams."""
    return Counter(word1) == Counter(word2)
```

Counter is essentially a multi-set in that it's sort of like a set that keeps track of the number of times each item (characters in this case) has been seen. If you'd like a refresher on the various ways of counting occurrences of things in Python, check out this article I wrote on counting things in Python.

You may have noticed that we don't necessarily need dictionaries of letter counts. The thing we really care about is whether the two words have the same letters and each occurs the same number of times. Comparing dictionaries of letter counts is just one way to determine whether the words have the same letters.

We could instead sort the letters in each word:

```python
def is_anagram(word1, word2):
    """Return True if the given words are anagrams."""
    return sorted(word1) == sorted(word2)
```

Python's built-in sorted function loops over whatever we give it (a string in this case) and gives us back a list of the sorted items (letters in this case). If the letters in each word are the same, the two sorted lists should be identical.

The Counter solution may be slightly more clear, but the sorted solution seems to be faster for short strings (though likely longer for very long strings). I think they're both very good solutions and I personally prefer the Counter solution because I find it more descriptive. I'll be using a mix of both solutions for the bonuses.

Up to this point our code has actually been failing one of our requirements. Our function is supposed to ignore case when we comparing the letters in our two words. How could we do that?

To ignore case in our words, we could normalize the letters in our words by lowercasing them in both words:

```python
def is_anagram(word1, word2):
    """Return True if the given words are anagrams."""
    word1, word2 = word1.lower(), word2.lower()
    return sorted(word1) == sorted(word2)
```

Notice that we're reassigning to the word1 and word2 two variables. We could have made new variable names, but it's not uncommon to reuse the old names when normalizing string inputs to a function.

Also notice that we're using tuple unpacking to assign both variables on one line of code. We could have done this on two lines. I did it on one line to emphasize the parity of the two arguments.

Okay so our function works. Let's work on the bonus. For the first bit of the bonus, we're supposed to make sure we ignore spaces.

We can do this by replacing all space characters with an empty string in our words:

```python
from collections import Counter

def is_anagram(word1, word2):
    """Return True if the given words are anagrams."""
    word1, word2 = word1.lower(), word2.lower()
    return Counter(word1.replace(' ', '')) == Counter(word2.replace(' ', ''))
```

We'll improve on this in the second bonus, which requires being even more specific about what we match.

For the second bonus we were supposed to ignore punctuation characters.

We can do this by using a generator expression that filters out non-alphabetical characters:

```python
def is_anagram(word1, word2):
    """Return True if the given words are anagrams."""
    word1, word2 = word1.lower(), word2.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters1 = sorted(c for c in word1 if c in alphabet)
    letters2 = sorted(c for c in word2 if c in alphabet)
    return letters1 == letters2
```

The "```(c for c in word1 if c in alphabet)```" is a **generator expression**, which is like a list comprehension that gives back a lazy generator instead of a list.

If you're new to Python, list comprehensions and generator expressions are probably new, weird, and scary. I have a talk called Comprehensible Comprehensions that explains how list comprehensions work and how generator expressions are different. I'd recommend watching that talk if you're new to these concepts.

We're using the condition "if c in alphabet" (where alphabet is a string of lowercase letters) to filter down our characters to just letters.

Strings in Python have an ```isalpha``` method that returns True if the given string is entirely alphabetical. We can use this to select just the alphabetical characters as we loop over our string:

```python
def is_anagram(word1, word2):
    """Return True if the given words are anagrams."""
    word1, word2 = word1.lower(), word2.lower()
    letters1 = sorted(c for c in word1 if c.isalpha())
    letters2 = sorted(c for c in word2 if c.isalpha())
    return letters1 == letters2
```

Knowing methods on Python's built-in types can come in handy sometimes. We could take this a step further by making the sorting lines into a function that we call twice:

```python
def letters_in(string):
    """Return sorted list of letters in given string."""
    return sorted(
        char
        for char in string.lower()
        if char.isalpha()
    )

def is_anagram(word1, word2):
    """Return True if the given words are anagrams."""
    return letters_in(word1) == letters_in(word2)
```

We were doing the same operation on both words so moving this logic into a separate functions makes sense for clarity.

If we use a Counter object we could rename our ```letters_in``` function to ```counter_letters```, which might be more clear:

```python
from collections import Counter

def count_letters(string):
    """Return sorted list of letters in given string."""
    return Counter(
        char
        for char in string.lower()
        if char.isalpha()
    )

def is_anagram(word1, word2):
    """Return True if the given words are anagrams."""
    return count_letters(word1) == count_letters(word2)
```

You might find answers for how to remove punctuation from a string on StackOverflow which talk about using the string's translate method. This works, but it's a little confusing and will be tricky to use for removing non-English punctuation (this answer does so but it's very slow the first time you run it).

The last part of the bonus is a bit harder. We were supposed to ignore accents on accented Latin characters.

We'll need to normalize our unicode data to such that characters are decomposed into parts (so accents are treated separately from the character they accent). If we look up unicode normalization or search for how to ignore accent marks in unicode strings we'll find **NFKD form**. The ```unicodedata``` module can help us normalize our strings into NFKD form (NFD form should work as well):

```python
import unicodedata

def remove_accents(string):
    """Return decomposed form of the given string."""
    return unicodedata.normalize('NFKD', string)

def letters_in(string):
    """Return sorted list of letters in given string."""
    string = remove_accents(string.lower())
    return sorted(
        char
        for char in string
        if char.isalpha()
    )

def is_anagram(word1, word2):
    """Return True if the given words are anagrams."""
    return letters_in(word1) == letters_in(word2)
```

Notice our is_anagram function hasn't changed at all here. We've added a remove_accents function and we're now calling it on our lowercased string in our letters_in function.

Did these solutions make you think about anything you hadn't thought of yet? Did you use generator expressions in your solution? Did you used collections.Counter or sorted? Did you attempt the bonus solutions?

Wait a day and then try solving this exercise again without looking at any of the answers. See how your solution compares.
