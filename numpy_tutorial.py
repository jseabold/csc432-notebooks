# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# NumPy
# ------
# * Arrays
# * Matrics - We won't use these
# * Indexing
# * Views vs. Copies
# * Some useful functions - arange, linspace
# * Constants
# * Modules (random, linalg, fft, poly, masked arrays)
# 
# &nbsp;
# 
# * http://www.scipy.org/NumPy_for_Matlab_Users
# * http://mathesaurus.sourceforge.net/
# * http://mathesaurus.sourceforge.net/r-numpy.html
# * http://scipy-lectures.github.com/intro/numpy/index.html

# <headingcell level=3>

# Import convention

# <codecell>

import numpy as np

# <headingcell level=3>

# Arrays

# <markdowncell>

# The basic data structure of NumPy is a n-dimensional array of homogeneous type. The dimensions of arrays are called **axes**.

# <codecell>

X = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

# <codecell>

type(X)

# <codecell>

X.ndim # number of dimensions

# <codecell>

X.shape # axes 0, 1

# <codecell>

X.dtype # the data type of the array

# <codecell>

X.size # the number of elements in the array

# <codecell>

X.itemsize # size in bytes of elements

# <markdowncell>

# Why use arrays? Speed.

# <codecell>

plain_list = range(1000)
# IPython magic
%timeit [i**2 for i in plain_list]

# <codecell>

arr = np.arange(1000)
%timeit arr**2

# <markdowncell>

# Make an array called `time_checks` that contain numbers from 0 to 4, in increments of .25. (Hint: range does not take float arguments!)

# <headingcell level=3>

# Array creation

# <markdowncell>

# From a list

# <codecell>

x = np.array([1, 3, 5])

# <markdowncell>

# This is a 1-dimensional array.

# <codecell>

x.shape

# <markdowncell>

# This is not the same as a 2-dimensional row vector.

# <codecell>

x = np.array([[1, 3, 5]])

# <codecell>

x

# <codecell>

x.shape

# <markdowncell>

# You could also initialize the array with tuples

# <codecell>

x = np.array(((1, 2, 3),(4, 5, 6)))

# <codecell>

x

# <markdowncell>

# While the type is inferred from the input data, you can also use the dtype argument.

# <codecell>

x = np.array([1, 3, 5], dtype=float)

# <codecell>

x.dtype

# <markdowncell>

# There are some convenience functions to initialize commonly needed arrays.

# <codecell>

X = np.empty((5, 3))
X

# <codecell>

X = np.zeros((5, 3), dtype=np.int16)
X

# <codecell>

X = np.ones((5, 3))
X

# <codecell>

Y = np.ones_like(X)
Y

# <markdowncell>

# Or arrays of sequences of numbers.

# <codecell>

X = np.arange(5)
X

# <codecell>

X = np.arange(5, 10)
X

# <markdowncell>

# With step-size

# <codecell>

X = np.arange(5, 25., 5)
X

# <markdowncell>

# By number of points

# <codecell>

X = np.linspace(0, 10, 25)
X

# <codecell>

X = np.eye(3)
X

# <codecell>

X = np.diag(np.arange(1,5.))
X

# <markdowncell>

# <div class="green topic">
# <p class="topic-title first"><strong>Exercise: Array creation</strong></p>
# <p>Create the following arrays (with correct data types):</p>
# <div class="highlight-python"><pre>[[ 1  1  1  1]
#  [ 1  1  1  1]
#  [ 1  1  1  2]
#  [ 1  6  1  1]]
# 
# [[0. 0. 0. 0. 0.]
#  [2. 0. 0. 0. 0.]
#  [0. 3. 0. 0. 0.]
#  [0. 0. 4. 0. 0.]
#  [0. 0. 0. 5. 0.]
#  [0. 0. 0. 0. 6.]]</pre>
# </div>
# <p>Par on course: 3 statements for each</p>
# <p><em>Hint</em>: Individual array elements can be accessed similarly to a list,
# e.g. <tt class="docutils literal"><span class="pre">a[1]</span></tt> or <tt class="docutils literal"><span class="pre">a[1,</span> <span class="pre">2]</span></tt>.</p>
# <p><em>Hint</em>: Examine the docstring for <tt class="docutils literal"><span class="pre">diag</span></tt>.</p>
# </div>
# <div class="green topic">
# <p class="topic-title first">Exercise: Tiling for array creation</p>
# <p>Skim through the documentation for <tt class="docutils literal"><span class="pre">np.tile</span></tt>, and use this function
# to construct the array:</p>
# <div class="highlight-python"><pre>[[4 3 4 3 4 3]
#  [2 1 2 1 2 1]
#  [4 3 4 3 4 3]
#  [2 1 2 1 2 1]]</pre>
# </div>
# </div>
# </div>

# <headingcell level=3>

# Printing arrays

# <codecell>

x = np.arange(6)
print x

# <codecell>

x = np.arange(12).reshape(4,3)
print x

# <codecell>

x = np.arange(24).reshape(4, 3, 2)
print x

# <codecell>

print np.arange(1500)

# <codecell>

x = np.random.random(5)

# <codecell>

print x

# <codecell>

print x[0]

# <codecell>

np.set_printoptions(precision=4)
print x

# <codecell>

np.set_printoptions(precision=12)

# <codecell>

print x[0]

# <codecell>

x[0]

# <headingcell level=3>

# Basic Operations

# <markdowncell>

# Operations apply to arrays *element-wise*

# <codecell>

x = np.arange(20, 101, 20)
x

# <codecell>

y = np.arange(100, 19, -20)
y

# <codecell>

y - x

# <codecell>

x ** 2

# <codecell>

x * np.sin(y) # this is element-wise!

# <codecell>

x < 50

# <codecell>

X / 2 # be careful

# <codecell>

A = np.array([[1., 2, 3],
              [4.5, 2.1, 3],
              [1, 3.3, 6.5]])

# <codecell>

B = np.array([[1.5, 2, 3],
              [4.5, 1.2, 2],
              [2.1, 3.5, 5]])

# <codecell>

A * B # element-wise

# <codecell>

np.dot(A, B) # dot product (aka matrix multiplication)

# <markdowncell>

# <h4>Aside: Matrix Multiplication</h4>
# 
# *Matrix multiplication* is done by taking the *dot product* of the rows and columns of two matrices. For any two matrices $\boldsymbol{A}$ and $\boldsymbol{B}$ the elements of the resultant matrix $\boldsymbol{C}=\boldsymbol{A}\boldsymbol{B}$ is formed by taking the inner-product of the rows of $\boldsymbol{A}$ and the columns of $\boldsymbol{B}$. To illustrate, assume $\boldsymbol{A}$ is a matrix of order $m\times n$ and $\boldsymbol{B}$ is a matrix of order $n\times p$. The element $(i,k)$ of matrix $\boldsymbol{C}$ is $\sum{j=1}^{n}a_{ij}b_{jk}$. This is what is meant by the inner product. As you can see, for this to work, the column dimension of $\boldsymbol{A}$ and the row dimension of $\boldsymbol{B}$ must be the same. If this is the case, then the matrices $\boldsymbol{A}$ and $\boldsymbol{B}$ are said to be *conformable*. **Note:** order matters for matrix multiplication. It is usually the case that $\boldsymbol{A}\boldsymbol{B}\neq \boldsymbol{B}\boldsymbol{A}$. For the expression $\boldsymbol{A}\boldsymbol{B}$, the matrix $\boldsymbol{A}$ is said to *premultiply* $\boldsymbol{B}$ and $\boldsymbol{B}$ is said to postmultiply $\boldsymbol{A}$.

# <markdowncell>

# Coding something is a great way to solidify your intuition of mathematics, if you aren't getting an immediate clarity of insight. It is second only to practicing operations by hand, but I will leave that for your linear algebra course. Go ahead and write a function to calculate the dot product $\boldsymbol{C}=\boldsymbol{A}\boldsymbol{B}$. This function should be general enough to find the dot product of any two matrices, not just two $3\times 3$ ones. (*Hint*: You will want to use two loops and the `shape` method of the arrays.)
#     
#     A = [[1, 2, 3],
#          [2, 4, 5],
#          [1, 0, 1]]
#     
#     B = [[7, 2, 1],
#          [3, 2, 0],
#          [2, 1, 2]]
# 
# Compare your answer to that obtained using numpy's dot.

# <codecell>

A = [[1, 2, 3],
     [2, 4, 5],
     [1, 0, 1]]

B = [[7, 2, 1],
     [3, 2, 0],
     [2, 1, 2]]

# <headingcell level=4>

# In-Place Operations

# <codecell>

A

# <codecell>

A *= 3
A

# <codecell>

B = np.arange(9, dtype=np.int32).reshape(3, 3)
B

# <codecell>

B += A # A is copied to an integer type array

# <codecell>

B

# <headingcell level=4>

# Upcasting behavior

# <codecell>

x = np.ones(5, dtype=np.int32)
y = np.linspace(0, np.pi, 5)

# <codecell>

print x.dtype

# <codecell>

print y.dtype

# <codecell>

z = x + y
z.dtype

# <codecell>

print z

# <headingcell level=4>

# Indexing and Slicing

# <markdowncell>

# 1-dimensional arrays can be sliced, iterated over, and indexed much like lists.

# <codecell>

a = np.arange(10)**.5
a

# <markdowncell>

# Like C/C++ Python sequences are zero-based!

# <codecell>

a[0]

# <codecell>

a[5]

# <markdowncell>

# Slicing

# <codecell>

a[3:5]

# <codecell>

a[:7]

# <codecell>

a[0:7:3]

# <codecell>

a[slice(0, 7, None)]

# <codecell>

a[::-1]

# <markdowncell>

# 2-D slicing is done with tuples

# <codecell>

X = np.diag(np.arange(5))
X

# <codecell>

X[3,3]

# <markdowncell>

# Use a colon to grab elements over the entire other dimensions. For example, to get column 3.

# <codecell>

X[:, 3]

# <markdowncell>

# You can omit trailing axes.

# <codecell>

X[4]

# <codecell>

X = np.arange(48).reshape(4,3,4)
X

# <codecell>

X[1,2]

# <markdowncell>

# Using ... means use : for each omitted axis. This is greedy.

# <codecell>

X = np.arange(2**5).reshape(2,2,2,2,2)
X

# <codecell>

X[0, :, :, :, 0]

# <codecell>

X[0, ..., 0]

# <headingcell level=4>

# Fancy Indexing

# <markdowncell>

# Fancy indexing allows the use of boolean and integer array-like objects as indices.

# <headingcell level=5>

# Boolean Indexing

# <codecell>

np.random.seed(1234)
a = np.random.randint(0, 20, 15)
a

# <codecell>

idx = a % 3 == 0
idx

# <codecell>

a[idx]

# <codecell>

a[idx] += 1
a

# <headingcell level=5>

# Indexing with Integer Masks

# <codecell>

a[[0, 2, 5, 10]]

# <codecell>

a[[2,0,2,0,2,0]] # repeat elements

# <codecell>

idx = np.array([[0,1],[8,9]])

# <codecell>

b = a[idx]

# <codecell>

b

# <markdowncell>

# But this won't work

# <codecell>

#a[idx.tolist()]

# <headingcell level=5>

# Adding an axis to an array

# <codecell>

X = np.arange(15)
X

# <codecell>

X.shape

# <codecell>

X[:,None].shape

# <codecell>

X[:,np.newaxis].shape

# <codecell>

X[None,:].shape

# <headingcell level=4>

# Copies vs Views

# <markdowncell>

# Slicing and indexing produces a view of the array in memory.

# <codecell>

X = np.arange(24).reshape(6,4)
X

# <codecell>

Y = X[:,2]
Y

# <codecell>

Y[Y > 10] = 1000
Y

# <codecell>

X

# <markdowncell>

# However, fancy-indexing always copies.

# <codecell>

X = np.arange(24).reshape(6,4)
X

# <codecell>

Y = X[:,[1, 3]]
Y

# <codecell>

Y[Y > 10] = 1000

# <codecell>

Y

# <codecell>

X

# <markdowncell>

# Careful, transposes are views too.

# <codecell>

X = np.ones((100,100))
X

# <markdowncell>

# So this won't work as expected to make a symmetric matrix.

# <codecell>

X += X.T
X

# <headingcell level=4>

# Example: Prime-Number Sieve

# <codecell>

from IPython.core.display import Image
Image("http://scipy-lectures.github.com/_images/prime-sieve.png")

# <codecell>

is_prime = np.ones((100.,), dtype=bool)

# <codecell>

is_prime[:2] = False # 0 and 1 aren't prime

# <codecell>

n_max = int(len(is_prime) ** .5) # largest number to check
n_max

# <codecell>

for i in range(2, n_max):
    is_prime[2*i::i] = False

# <markdowncell>

# Make sure you understand what the above is doing. Write it down and convince yourself of this.

# <markdowncell>

# Use np.nonzero to print the primes from 2 to 100.

# <codecell>

np.nonzero(is_prime)

# <markdowncell>

# Modify the above to implement [the sieve of Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).

# <headingcell level=4>

# Universal Functions (or "ufuncs")

# <markdowncell>

# NumPy provides many mathematical functions that are also found in the built-in math library. These ufuncs are array-aware and are optimized for speed.

# <codecell>

np.random.seed(12345)
X = np.random.random(25)

# <codecell>

np.sqrt(X)

# <codecell>

Y = np.random.random(25)

# <codecell>

%timeit np.add.reduce(X)

# <codecell>

%timeit np.sum(X)

# <codecell>

%timeit X.sum()

# <headingcell level=4>

# Useful Constants

# <codecell>

np.pi

# <codecell>

np.e

# <headingcell level=4>

# Modules

# <codecell>

import inspect

# <markdowncell>

# The documentation for the built-in `inspect` module is [here](http://docs.python.org/2/library/inspect.html).

# <codecell>

for name, obj in inspect.getmembers(np):
    if inspect.ismodule(obj):
        print name

# <markdowncell>

# You will be most interested in `fft`, `linalg`, `polynomial`, `random`, `testing`, and possibly `ma`.

