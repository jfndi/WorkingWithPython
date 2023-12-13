"""
basic_usage.py:

    Created on 11-Dec-23
    
    @Author: Jean-François Ndi
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#
# An Axes is an Artist attached to a Figure that contains a region for plotting
# data and usually includes two (or three in the case of 3D) Axis objects that
# provides ticks and tick labels to provide scales for the data in the Axes.
# Each Axes also has a title, an x-label and a y-label.
# Axis set the scale, limits and generate ticks and tick-labels. The location
# of the ticks is determined by a Locator object and the tick-label strings are
# formatted by a Formatter.
# Artist is everything that is visible on the Figure. This includes Text,
# Line2D, collections, Patch objects etc...
# The simplest way of creating a Figure with an Axes is using pyplot.subplots.
# We can, then, use Axes.plot to draw some data on the Axes.
# The Figure keeps track of all the child Axes, a group of special Artists and
# even nested sub-figures.
#
_, ax = plt.subplots()  # A figure with a single Axes. Figure is ignored.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()  # This will block until the Figure is closed.

#
# Plotting functions expect numpy.array or numpy.ma.masked_array as input, or
# objects that can be passed to numpy.asarray. Classes that are similar to
# arrays such as pandas data objects and numpy.matrix may not work as intended.
# Common convention is to convert these to numpy.array objects prior plotting.
# Most methods will also parse a string-indexable object like a dict, a
# structured numpy array or a pandas.DataFrame. Matplotlib allows us to provide
# the data keyword argument and generate plots passing the strings
# corresponding to the x and y variables.
#
np.random.seed(19680801)  # Seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

_, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
plt.show()

#
# There are essentially two ways to use Matplotlib:
# * Explicitly create Figures and Axes and call methods on them (OO style).
# * Rely on pyplot to implicitly create and manage the Figures and Axes and use
#   pyplot functions for plotting.
# OO style:
#
x = np.linspace(0, 2, 100)  # Sample data.
_, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(x, x, label='linear')  # Plot some data on the Axes.
ax.plot(x, x**2, label='quadratic')  # and more data...
ax.plot(x, x**3, label='cubic')  # and even more.
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title('Simple Plot (OO style)')
ax.legend()
plt.show()

#
# Pyplot style:
#
x = np.linspace(0, 2, 100)  # Sample data.
plt.figure(figsize=(5, 2.7), layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the Axes.
plt.plot(x, x**2, label='quadratic')  # and more data...
plt.plot(x, x**3, label='cubic')  # and even more.
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot (Pyplot style)")
plt.legend()
plt.show()

#
# Sometimes, we have to make the same plot over and over with different data
# sets, or want to easily wrap Matplotlib methods. We can use the recommended
# signature function below:
#


def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph.

    :param ax: The Axis.
    :param data1: The x data.
    :param data2: The y data.
    :param param_dict: The plot parameters.
    :return: Line2D list.
    """
    out = ax.plot(data1, data2, **param_dict)
    return out


data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets.
_, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})
plt.show()

#
# Most plotting methods have styling options for the Artists accessible either
# when plotting method is called or from a "setter" on the Artist. In the plot
# below, we manually set the color, linewidth and linestyle of the Artists
# created by plot, and we set the linestyle of the second line after the fact
# with set_linestyle/
#
_, ax = plt.subplots(figsize=(5, 2.7))
x = np.arange(len(data1))
ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
l.set_linestyle(':')
plt.show()

#
# Matplotlib has a very flexible array of colors that are accepted for most
# Artists. Some Artists will take multiple colors i.e. for scatter plot, the
# edge of the marker can be different colors from the interior.
#
_, ax = plt.subplots(figsize=(5, 2.7))
ax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k')
plt.show()

#
# Line widths are typically in typographic points and available for Artists
# that have stroked lines. Similarly, stroked lines have a linestyle.
#
_, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(data1, 'o', label='data1')
ax.plot(data2, 'd', label='data2')
ax.plot(data3, 'v', label='data3')
ax.plot(data4, 's', label='data4')
ax.legend()
plt.show()

#
# set_xlabel, set_ylabel and set_title are used to add text in the indicated
# locations. Text can also be directly added to plots using text.
#
mu, sigma = 115, 15
x = mu + sigma * np.random.randn(10000)
_, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)

ax.set_xlabel('Length [cm]')
ax.set_ylabel('Probability')
ax.set_title('Aadvark lengths\n (not really)')
ax.text(75, 0.025, r'$\mu=115,\ \sigma=15$')
ax.axis([55, 175, 0, 0.03])
ax.grid(True)
plt.show()

#
# We can also annotate points on a plot, often by connecting an arrow pointing
# to xy, to a piece of text at xytext.
#
_, ax = plt.subplots(figsize=(5, 2.7))
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
ax.plot(t, s, lw=2)
ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.set_ylim(-2, 2)
plt.show()

#
# Often we want to identify lines or markers with Axes.legend.
#
_, ax = plt.subplots(figsize=(5, 2.7))
ax.plot(np.arange(len(data1)), data1, label='data1')
ax.plot(np.arange(len(data2)), data2, label='data2')
ax.plot(np.arange(len(data3)), data3, 'd', label='data3')
ax.legend()
plt.show()

#
# Each Axes has two (or three) Axis objects representing the x- and y-axis.
# These control the scale of the AXis, the tick locator and the tick formatters.
# Additional Axes can be attached to display further Axis objects.
# In addition to the linear scale, Matplotlib supplies non-linear scales, such
# loglog, semilogx and semilogy.
#
_, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')
xdata = np.arange(len(data1))
data = 10**data1
axs[0].plot(xdata, data)

axs[1].set_yscale('log')
axs[1].plot(xdata, data)
plt.show()

#
# Each Axis has a tick locator and formatter that choose where along the Axis
# objects to put tick marks.
#
_, axs = plt.subplots(2, 1, layout='constrained')
axs[0].plot(xdata, data1)
axs[0].set_title('Automatic ticks')

axs[1].plot(xdata, data1)
axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])
axs[1].set_yticks([-1.5, 0, 1.5])
axs[1].set_title('Manual ticks')
plt.show()

#
# Matplotlib can handle plotting arrays of dates and arrays of strings, as well
# as floating point numbers. These get special locators and formatters as
# appropriate. For dates:
#
_, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
dates = np.arange(np.datetime64('2021-11-15'), np.datetime64('2021-12-25'),
                  np.timedelta64(1, 'h'))
data = np.cumsum(np.random.randn(len(dates)))
ax.plot(dates, data)
cdf = mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator())
ax.xaxis.set_major_formatter(cdf)
plt.show()

#
# For strings:
#
_, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
categories =['turnips', 'rutabaga', 'cucumber', 'pumpkins']
ax.bar(categories, np.random.rand(len(categories)))
plt.show()

#
# Plotting data of different magnitude in one chart may require an additional
# y-axis. Such an Axis can be created by using twinx to add new Axes with an
# invisible x-axis and a y-axis positioned at the right.
# Similarly, you can add a secondary_xaxis or secondary_yaxis having a
# different scale than the main Axis to represent the data in different scales
# or units.
#
_, (ax1, ax3) = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')
l1, = ax1.plot(t, s)
ax2 = ax1.twinx()
l2, = ax2.plot(t, range(len(t)), 'C1')
ax2.legend(([l1, l2]), ['Sine (left)', 'Straight (right)'])

ax3.plot(t, s)
ax3.set_xlabel('Angle [rad]')
ax4 = ax3.secondary_xaxis('top', functions=(np.rad2deg, np.deg2rad))
ax4.set_xlabel('Angle [°]')
plt.show()

#
# Often we want to have a third dimension in a plot represented by a colors in
# colormap. Matplotlib has a number of plot types that do this:
#
X, Y = np.meshgrid(np.linspace(-3, 3, 128), np.linspace(-3, 3, 128))
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

fig, axs = plt.subplots(2, 2, layout='constrained')
pc = axs[0, 0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[0, 0])
axs[0, 0].set_title('pcolormesh')

co = axs[0, 1].contourf(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11))
fig.colorbar(co, ax=axs[0, 1])
axs[0, 1].set_title('contourf')

pc = axs[1, 0].imshow(Z**2 * 100, cmap='plasma',
                      norm=mpl.colors.LogNorm(vmin=0.01, vmax=100))
fig.colorbar(pc, ax=axs[1, 0], extend='both')
axs[1, 0].set_title('imshow() with LogNorm()')

pc = axs[1, 1].scatter(data1, data2, c=data3, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[1, 1], extend='both')
axs[1, 1].set_title('scatter')
plt.show()
