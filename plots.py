import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

#%matplotlib inline

# Graph Styling

plt.style.use("seaborn-darkgrid")


# Line Graphs

# By default Plot() function will draw a line chart.

x = np.array([1,2,3,4,5,6])
y = np.power(x,3)

plt.plot(x,y)
plt.show()


x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x,y)
plt.show()

# Recover default matplotlib settings
mpl.rcParams.update(mpl.rcParamsDefault)

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x,y)
plt.show()

plt.style.use("seaborn-darkgrid")

plt.figure(figsize=(10,5))

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x,y)
plt.show()

# Solid blue line will be plotted using the argument "b-"

plt.figure(figsize=(10,5))

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x,y, "b-")
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.show()


# Solid blue line will be plotted using the argument "r-"

plt.figure(figsize=(10,5))

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x,y, "r-")
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.show()

# Plot green dots using the argument "go"

plt.figure(figsize=(10,5))

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x,y, "go")
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.show()

# Plotting red dots using the argument "ro"

plt.figure(figsize=(10,5))

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x,y, "ro")
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.show()

# Plotting traingular dots using the argument "r^"

plt.figure(figsize=(10,5))

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x,y, "r^")
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.show()

# Plotting traingular dots using the argument "rv"

plt.figure(figsize=(10,5))

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x,y, "rv")
plt.xlabel('X - Axis')
plt.ylabel('Y - Axis')
plt.show()

#Plotting multiple sets of data

plt.figure(figsize=(10,5))
x = np.array([1,2,3,4,5,6])
y1 = np.power(x,2)
y2 = np.power(x,3)
plt.plot(x,y1, "b-" , label = '$y1 = x^2$') # Setting up legends
plt.plot(x,y2, "r-" ,label ='$y2 = x^3$') # Setting up legends
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.legend()
plt.tight_layout()
plt.show()