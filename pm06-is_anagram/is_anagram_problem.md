I want you to write a function that accepts two strings and returns True if the two strings are anagrams of each other.

Your function should work like this:
>>> is_anagram("tea", "eat")
True
>>> is_anagram("tea", "treat")
False
>>> is_anagram("sinks", "skin")
False
>>> is_anagram("Listen", "silent")
True
Make sure your function works with mixed case.

Before you try to solve any bonuses, I recommend you try to find at least two ways to solve this problem.

Okay now to the bonuses...

For the first bonus, make sure your function ignores spaces ✔️:
>>> is_anagram("coins kept", "in pockets")
True

For the second bonus, make sure your function also ignores punctuation ✔️:
>>> is_anagram("a diet", "I'd eat")
True

If you solved this one really quickly, here's a more challenging third bonus for you: try allowing accented latin characters but ignoring the accent marks. ✔️
>>> is_anagram("cardiografía", "radiográfica")
True

