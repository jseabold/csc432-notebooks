# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=4>

# 2.3.10 - Using Computational Tool vs. Analytic solution

# <codecell>

from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

# <markdowncell>

# $$\frac{dP}{dt}=.3P-20$$
# 
# where
# 
# $$P_0=25$$
# 
# $$\frac{dP}{.3P-20}\;=dt$$

# <codecell>

def p_func(t):
    """
    dP/dt = .3P - 20, P_0 = 25
    P     = (20 - 9.5*np.exp(.3*t))/.3
    """
    return (20 - 9.5*np.exp(.3*t))/.3

# <codecell>

time_grid = np.arange(0, 10, .01)

fig, ax = plt.subplots()
ax.plot(time_grid, p_func(time_grid), label="analytic solution")
ax.legend();

# <codecell>

def dPdt(P, t):
    return .3*P - 20

# <codecell>

results = integrate.odeint(dPdt, 35, time_grid, full_output=1)
p_function = results[0]

# <codecell>

fig, ax = plt.subplots()

ax.plot(time_grid, p_function, label="numerical solution")
ax.legend();

# <codecell>

fig, ax = plt.subplots()
ax.plot(time_grid, p_func(time_grid), label="analytic solution")
ax.plot(time_grid, p_function, label="numerical solution")
ax.legend();

