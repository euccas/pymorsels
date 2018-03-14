If you haven't attempted to solve count_words yet, close this email and go do that now before reading on. If you have attempted solving count_words, read on...

We're going to talk about solving this by manually building up a dictionary first. Then we'll discuss some helper utilities we could have used instead. After that we'll discuss the two bonus solutions.

If we solve this using a dictionary. We'll need to handle two cases:
The word is not yet in the dictionary. We need to add it with a value of 1 in this case.
The word is already in the dictionary. We need to increment its value in this case.
Here's one possible answer using a dictionary:

```python
def count_words(string):
    """Return the number of times each word occurs in the string."""
    count = {}
    for word in string.split():
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
```

Notice that we use the string split method to get words. The split method splits on any number of consecutive white space (including spaces, linebreaks, tabs, etc) by default.

The if statement checks for the presence of a key corresponding to each word. The if statement could have been written without an else instead:

```python
def count_words(string):
    """Return the number of times each word occurs in the string."""
    count = {}
    for word in string.split():
        if word not in count:
            count[word] = 0
        count[word] += 1
    return count
```

Dictionaries also have a get method that can be used to lookup the value for a given key or get a specific default value if the key isn't in the dictionary. This could be used instead of that if statement:

```python
def count_words(string):
    """Return the number of times each word occurs in the string."""
    count = {}
    for word in string.split():
        count[word] = count.get(word, 0) + 1
    return count
```

Dictionaries also have a setdefault method that can be used to add a key-value pair to the dictionary with a given default value if the key isn't in the dictionary:

```python
def count_words(string):
    """Return the number of times each word occurs in the string."""
    count = {}
    for word in string.split():
        count.setdefault(word, 0)
        count[word] += 1
    return count
```

There are even more ways this could have been solved with dictionaries than these ones I've mentioned so far, but I'm going to stop talking about the various ways to solve this with plain old dictionaries and discuss other ways we can solve this. Let's talk about the collections module.

There's a defaultdict class in the collections module that creates a dictionary-like object that includes a recipe for calculating default values to set for keys that are accessed before they are put in the dictionary. We can use defaultdict(int) to solve this particular exercise:

```python
def count_words(string):
    """Return the number of times each word occurs in the string."""
    count = defaultdict(int)
    for word in string.split():
        count[word] += 1
    return count
```

That's pretty neat. We essentially don't need any of the defaulting in our dictionary because defaultdict does that for us. We can make this even simpler though. The Counter object will do all of the work we're doing for us:

```python
def count_words(string):
    """Return the number of times each word occurs in the string."""
    return Counter(string.split())
```

Counter objects are essentially a dictionary-like object specifically meant for counting the number of times things are seen and storing the things as keys and the times seen as values. You can think of it as essentially a set that counts the number of times it sees each thing, a multi-set of sorts.

Okay so that was a lot. If you're still interested in the various ways to solve this problem and you'd like to dive through history slightly, you might want to check out an article I wrote on specifically this problem.

Now let's talk about the bonus problems...

If we want to ignore the case of words, we could normalize the case by lowercasing all the words:

```python
def count_words(string):
    """Return the number of times each word occurs in the string."""
    return Counter(string.lower().split())
```

This has the side effect of losing information about the cases of the words we're counting, but it's hard to solve this problem without losing that information.

Okay now what if we want to ignore punctuation? This one was a little harder.

We could strip punctuation characters from the ends of words after we loop through them:

```python
def count_words(string):
    """Return the number of times each word occurs in the string."""
    words = []
    for word in string.lower().split():
        words.append(word.strip(',;.!?"()'))
    return Counter(words)
```

This will require us to list all punctuation characters we'd like to strip from the ends of words.

We could take a different approach. Instead of splitting our string by whitespace, we could use a regular expression to search for consecutive letters and symbols that should be considered as part of words:

```python
def count_words(string):
    """Return the number of times each word occurs in the string."""
    return Counter(re.findall(r"[\w'-]+", string.lower()))
```

We're lowercasing the string first and then using findall to find word-like letters (\w includes letters, digits, and underscore and we've included apostrophe and dash) one or more times consecutively (that's what + means).

Did you learn anything from these solutions? Wait a day and then try solving these again using something you learned.
