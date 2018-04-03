Let's start with an answer that doesn't quite work.

```python
import math

class Circle:
    """Circle with radius, area, and diameter."""
    def __init__(self, radius):
        self.radius = radius
        self.area = math.pi * self.radius ** 2
        self.diameter = self.radius * 2
```

Here we're setting all of our attributes in our initializer method, which gets run each time a new instance of our class is created.

This answer is missing two features that we need: it doesn't default the radius value to 1 (radius is required) and it doesn't have a useful string representation.

The default string representation of our class looks something like this:

```
>>> c = Circle(1)
>>> c
<circle.Circle object at 0x7f75816c48d0>
```

Which isn't very helpful for programmers who are using our class. We can fix this by adding a ```__repr__``` method. We'll do that and then also add a default value for the radius in our initializer method:

```python
import math

class Circle:

    """Circle with radius, area, and diameter."""

    def __init__(self, radius=1):
        self.radius = radius
        self.area = math.pi * self.radius ** 2
        self.diameter = self.radius * 2

    def __repr__(self):
        return f'Circle({self.radius})'
```

Here we're controlling the string representation of our class to return something that looks like the code we'd execute to recreate an equivalent class. **Note that we're using an f-string for string formatting. This is an alternative to using the format method or the % sign and this feature is only available in Python 3.6+.** Our string representation is much nicer now:

```
>>> c = Circle()
>>> c
Circle(1)
```

Additionally we also don't need to specify a radius (it defaults to 1).

Also note that **we don't need to implement __str__, the other string representation**. **By default __str__ relies on __repr__,** so if they're the same we only need to define __repr__.

This code passes all of our basic tests now.

Let's talk about the first bonus now.

## Bonus #1
The first bonus required that when we change the radius, the diameter and area change automatically.

To do this we need to make the diameter and area attributes into properties. We can do that by using the property decorator:

```python
class Circle:

    """Circle with radius, area, and diameter."""

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return f'Circle({self.radius})'

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2
```

With this new class, whenever the area and diameter attributes are accessed, the corresponding methods will be executed and the returned value will be provided as the value of the accessed attribute.

If you've never seen **properties** before, you should definitely look them up. They're Python's **preferred equivalent to getter and setter methods** (which are popular in the Java world for example).

Let's attempt the second bonus now.

## Bonus #2
The second bonus required that the diameter property be able to be set to a value and that the radius would automatically change appropriately based on the set value.

For this we need to make a setter for our diameter property. Here are just the diameter property methods in our class:

```python
    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2
```

The syntax for property setters is a little weird. If you're unfamiliar with that ```@``` we've been using, that's the **syntax for using a decorator** in Python. Python's built-in property class can be used as a decorator, but it can also be used with a different syntax:

```python
    def get_diameter(self):
        return self.radius * 2

    def set_diameter(self, diameter):
        self.radius = diameter / 2

    diameter = property(get_diameter, set_diameter)
```

Personally I prefer the decorator syntax for properties so I use that @ syntax pretty much exclusively. This one works fine too though.

Now let's take a look at the final bonus now.

## Bonus #3
For this bonus, we're supposed to make it so that the radius attribute cannot be set to a negative number. This one might have required a bit more thought, even if you've used properties before.

The key to this one was to realize that the radius attribute could also be powered by a property:

```python
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius
```

Adding a getter and setter for the radius property is all we need to do to get the bonus working. Whenever we set radius (like in our __init__ method or our diameter setter)  or access the radius (like in our diameter and area getters), these getter and setter methods will be called.

You might think you need to update your __init__ method to also assign to self._radius and handle that exceptional case. But we don't! The reason we don't is that by the time __init__ is called, our class instance has been constructed and assigning to self.radius will call our radius setter automatically! We're able to treat our _radius attribute as encapsulated in the property getter/setters. We can change _radius outside, but there's not a good reason to do so.

Properties are really powerful in Python. Python's properties allow us to take an existing attribute-based class API and maintain backwards compatibility while adding new functionality during attribute lookup or assignment.

We now have a complete implementation of the Circle class which should pass all of our tests.

I hope you learned something from this exercise about classes and properties from these solutions. 😄