# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=3>

# Polynomial Equations

# <markdowncell>

# * An expression involving a sum of powers in one or more variables multiplied by coefficients
# * For example, a univariate polynomial is of the form
# 
# $$f(x)=a_nx^n+\cdots+a_2x^2+a_1x+a_0$$
# 
# or, more succinctly 
# 
# $$f(x)=\sum_{i=0}^n{a_i}x^i$$
# 
# * The highest power for which $a_i\neq0$ is called the **order** of the polynomial

# <codecell>

import numpy as np

# <codecell>

poly = np.polynomial.Polynomial([-2, -1, 1])

# <codecell>

fig, ax = plt.subplots()
x = np.linspace(-5.5, 5, 100)
ax.plot(x, poly(x), 'r')
ax.hlines(0, -5.5, 4.5, 'k', lw=2)
ax.vlines(0, -5, 20, 'k', lw=2)
ax.set_xlim(-5.5, 4.5)
ax.set_ylim(-4, 6.5)
ax.set_title("$f(x)=x^2-x-2$");

# <markdowncell>

# Given a high enough order, you can approximate *any* continuous function with a polynomial. See the [Stone-Weierstrass theorem](http://en.wikipedia.org/wiki/Stone%E2%80%93Weierstrass_theorem) for a discussion of this fact and more general results.

# <codecell>

poly2 = np.polynomial.Polynomial([0, -36, 0, 49, 0, -14, 0, 1])

# <codecell>

x2 = np.linspace(-3.2, 3.2, 1000)

fig, ax = plt.subplots()
ax.plot(x2, poly2(x2), 'r')
ax.hlines(0, -5.5, 4.5, 'k', lw=2)
ax.vlines(0, -100, 100, 'k', lw=2)
ax.set_xlim(-3.2, 3.2)
ax.set_ylim(-100, 100)
ax.set_title("$f(x)=x^7-14x^5+49x^3-36x$");

# <markdowncell>

# Quite often we are interested in the **roots** of polynomial functions. The root of a polynomial function $P(z)$ is a number $z_i$ such that $P(z_i)=0$.
# 
# For instance, in your homework (2.4.1.g), you were asked to determine when a ball hits water given that its trajectory is determined by the equation
# 
# $$-4.9t^2+15t+11$$
# 
# You could solve this using the quadratic formula, or you could use a root-finding algorithm. Luckily, NumPy has root-finding algorithms specifically for polynomials built-in.

# <codecell>

trajectory = np.polynomial.Polynomial([11, 15, -4.9])
trajectory.roots()

# <markdowncell>

# Or we can use the simpler, dedicated function for this. Note the reversal of the arguments.

# <codecell>

np.roots([-4.9, 15, 11])

# <markdowncell>

# We know from the [fundamental theorem of algebra](http://en.wikipedia.org/wiki/Fundamental_theorem_of_algebra) that every polynomial of order $n$ has $n$ roots. How do we know which root to use in the above?

# <markdowncell>

# An interesting observation is that if you reverse the coefficients of a polynomial, its roots are the reciprocal of the roots of the original polynomial. Whether you are working with roots or inverse roots of polynomials often depends on notational conventions for applications that involve polynomial roots, so it's something to watch out for.

# <codecell>

np.roots([-4.9, 15, 11])

# <codecell>

1/np.roots([11, 15, -4.9])

