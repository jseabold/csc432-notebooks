# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# See this lecture for further treatment of some more [advanced constructs in Python](http://scipy-lectures.github.io/advanced/advanced_python/index.html)

# <headingcell level=4>

# Iterators

# <markdowncell>

# * An iterator follows the [Iterator Protocol](http://docs.python.org/dev/library/stdtypes.html#iterator-types)
# * Any object that has a [next](http://docs.python.org/2.7/library/stdtypes.html#iterator.next) method ([`__next__`](http://docs.python.org/dev/library/stdtypes.html#iterator.__next__) in Python 3), and [`__iter__`](http://docs.python.org/dev/reference/datamodel.html#object.__iter__) method that returns self, and raises [StopIteration](http://docs.python.org/dev/library/exceptions.html#StopIteration) exception when there's nothing left to return
# * An easy way to get hold of an iterator object, is to call the `__iter__` method on a sequence

# <codecell>

nums = [1, 2, 3]

iter(nums)

# <codecell>

nums.__iter__()

# <codecell>

nums.__reversed__()

# <codecell>

it = iter(nums)

# <codecell>

next(it)

# <codecell>

it.next()

# <codecell>

next(it)

# <codecell>

next(it)

# <markdowncell>

# * You can use iteration objects in a `for..in` construct, in which case, the Exception is not raised
# * Iteration is pervasive in Python
# * For example, file objects and file-like objects are implemented as iterators

# <codecell>

fin = open("./week01-02-python_tutorial.ipynb", "r")

# <codecell>

next(fin)

# <codecell>

next(fin)

# <codecell>

for line in fin:
    pass

# <codecell>

line

# <codecell>

fin.close()

# <headingcell level=4>

# Generators

# <markdowncell>

# * Generators allow for lazy evaluation
# * You can think of them like a sequence that returns items one at a time
# * They are functions that contain the keyword `yield`

# <codecell>

def gener():
    yield 1
    yield 2

# <codecell>

it = gener()

# <codecell>

next(it)

# <codecell>

it.next()

# <codecell>

next(it)

# <codecell>

def f():
    print "-- start --"
    yield 3
    print "-- middle --"
    yield 4
    print "-- finished --"

# <markdowncell>

# Calling the function, does not execute its code

# <codecell>

it = f()

# <codecell>

next(it)

# <codecell>

next(it)

# <codecell>

next(it)

# <markdowncell>

# * Why use generators?
# * Generators avoid building an entire sequence in-memory
# * You might have to process this entire sequence item-by-item anyway

# <headingcell level=4>

# Example: Fibonacci Numbers

# <markdowncell>

# * A Fibonacci Sequence is defined by the recurrence relation
# 
# $$F_n = F_{n-1}+F_{n-1}$$

# <codecell>

def fibn(n):
    a = b = 1
    result = []
    for i in xrange(n):
        result.append(a)
        a, b = b, a + b
    return result

# <markdowncell>

# * Notice the use of `xrange` instead of `range`
# * In Python 2, `xrange` is a generator, itself

# <codecell>

fibn(12)

# <codecell>

def fibn(n):
    a = b = 1
    for i in xrange(n):
        yield a
        a, b = b, a + b

# <codecell>

for i in fibn(12):
    print i

# <codecell>

fibn_it = fibn(12)

# <codecell>

next(fibn_it)

# <codecell>

for i in fibn_it:
    print i

# <markdowncell>

# * Generators are consumed in iteration

# <codecell>

for i in fibn_it:
    print i

# <codecell>

next(fibn_it)

# <headingcell level=4>

# List Comprehensions

# <markdowncell>

# * You have seen list comprehensions used before

# <codecell>

[str(x) for x in range(12)]

# <markdowncell>

# * Why use a list comprehension instead of a for-loop?
# * If what you are doing inside the loop is simple, the overhead of the for-loop can be substantial
# * If it's really simple, just use `map`

# <codecell>

map(str, range(12))

# <markdowncell>

# * Sometimes, you need to be a little more complicated though

# <codecell>

[str(x) for x in range(12) if x % 2 == 0]

# <headingcell level=4>

# Generator Expressions

# <markdowncell>

# * Much like list comprehensions, you can also build generator expressions
# * Use `()` in place of `[]`

# <codecell>

(str(x) for x in range(12) if x % 2 == 0)

# <codecell>

it = (str(x) for x in range(12) if x % 2 == 0)

# <codecell>

next(it)

# <codecell>

for i in it:
    print i

# <markdowncell>

# * Any function that operates on a sequence can take a generator function
# * This can often be much more memory efficient, because the entire intermediate list is not built

# <codecell>

sum(x for x in range(12))

# <headingcell level=4>

# Back to Iterator Objects

# <markdowncell>

# * Why would you want to build your own iterator object?
# * Sometimes, you need to do state manipulations during iteration

# <codecell>

class Reverse:
    """Iterator for looping over a sequence backwards."""
    
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        return self
    
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

# <codecell>

my_list = ["dog", "cat", "monkey", "duck", "mouse", "lion"]

Reverse(my_list)

# <codecell>

rev_list = Reverse(my_list)

for i in rev_list:
    print i

