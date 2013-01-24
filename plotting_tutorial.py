# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Introduction to Matplotlib

# <headingcell level=4>

# Import Convention

# <markdowncell>

# For interactive work, you'll likely only want to import `pyplot`.

# <codecell>

import matplotlib.pyplot as plt

# <headingcell level=3>

# Interactive Plotting with PyPlot

# <markdowncell>

# Matplotlib is the standard plotting library for Python. If you are going to be doing some quick plotting during an interactive sessions, then you can use [matplotlib.pyplot](http://matplotlib.org/api/pyplot_api.html#module-matplotlib.pyplot). Pyplot collects much of the plotting functions into a single namespace and works very similarly to MATLAB plotting commands. The pyplot commands are stateful, so you are always working with the current figure and plotting area. You probably will want to avoid using pyplot in scripts and library code, however.

# <markdowncell>

# **NOTE:** If you're using the notebook profile that I provided you, you'll notice that I have set matplotlib loop integration to `'inline'`. This means that plots are immediately shown as soon as they are created. In the notebook, this means that you should update all the plots in the same `cell`. If you're working at the interpreter and you have interactive set to True, when you change a plot you may need to call `plt.draw_if_interactive` to update the plot. If you are not working in with interactive set to True, then you will need to call `plt.show()` to display your plots.

# <codecell>

x = np.linspace(1, 3, 30)
y = np.linspace(1, 10, 30)
lines = plt.plot(x, y)
points = plt.plot(x, y, 'o')

# <headingcell level=3>

# Library plotting

# <codecell>

fig, ax = plt.subplots()
lines = ax.plot(x, y)
points = ax.plot(x, y, 'd', color='red', markersize=14)
#lines[0].set_linewidth(10)

# <codecell>

fig = plt.figure()
ax = fig.add_subplot(111)
lines = ax.plot(x, y)
points = ax.plot(x, y, 'o')

# <codecell>

line = lines[0]
line?

# <headingcell level=4>

# Multiple Axes

# <codecell>

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10,6))
lines1 = ax1.plot(np.linspace(0, 1, 100), np.random.random(size=100))
lines2 = ax2.plot(np.linspace(0, 1, 100), np.random.random(size=100), 'r')

# <headingcell level=4>

# Plot an Image

# <codecell>

np.random.seed(12345)
image = np.random.random((50,50))

# <codecell>

print image[:5, :5]

# <codecell>

fig, ax = plt.subplots()
img = ax.imshow(image)
fig.colorbar(img);

# <codecell>

from scipy import sparse
image = sparse.rand(60, 60, density=.05).toarray()
print image[:6,:6]

# <codecell>

fig, ax = plt.subplots()
img = ax.imshow(image, cmap=plt.cm.gray)
fig.colorbar(img);

# <codecell>

from scipy import misc
import Image

fig, ax = plt.subplots()

img = Image.open("cage.jpeg")
ax.imshow(img)

#img = misc.lena()
#ax.imshow(img, cmap=plt.cm.gray)
ax.grid(False)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# <markdowncell>

# Convert to Lab format to change the color map.

# <codecell>

cage = Image.open("cage.jpeg")
cage_L = cage.convert("L")
fig, ax = plt.subplots()
# sepia filter
ax.imshow(cage_L, cmap=plt.cm.pink)
ax.grid(False)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# <headingcell level=2>

# 3-D Plotting with Matplotlib

# <markdowncell>

# Matplotlib is usually fine for basic 3D plotting, but if you want to do serious 3-d applications, you might consider looking at [Mayavi](http://docs.enthought.com/mayavi/mayavi/).

# <codecell>

import numpy as np
from scipy import stats

x1, x2 = np.random.multivariate_normal([0, 0], [[1,0],[0,1]], size=500).T
xmin = x1.min()
xmax = x1.max()
ymin = x2.min()
ymax = x2.max()
X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])
values = np.vstack([x1, x2])
kernel = stats.gaussian_kde(values)
Z = np.reshape(kernel(positions).T, X.shape)

# <codecell>

from mpl_toolkits.mplot3d import Axes3D
fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))
plot3d = ax.plot_surface(X, Y, Z, cmap=plt.cm.jet, rstride=2, cstride=2, 
                         alpha=.4)
cset = ax.contour(X, Y, Z, zdir='x', offset=-3, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=2, cmap=cm.coolwarm)

