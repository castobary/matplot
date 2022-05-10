import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


# Basic Bar Plot
id1 = np.arange(1,10)
score = np.arange(20,110,10)
plt.bar(id1,score)
plt.xlabel('Student ID') 
plt.ylabel('Score') 
plt.show()


# Custom Colored Bar Plot

id1 = np.arange(1,10)
score = np.arange(20,110,10)
plt.figure(figsize=(8,5)) # Setting the figure size
ax = plt.axes()
ax.set_facecolor("#ECF0F1") # Setting the background color by specifying the HEX Code 
#ax.set_facecolor("#999999")
plt.bar(id1,score,color = '#FFA726')
plt.xlabel(r'$Student $ $ ID$')
plt.ylabel(r'$Score$')
plt.show()

#Plotting multiple sets of data
x1= [1,3,5,7]
x2=[2,4,6,8]
y1 = [7,7,7,7]
y2= [17,18,29,40]
plt.figure(figsize=(8,6))
ax = plt.axes()
ax.set_facecolor("white")
plt.bar(x1,y1,label = "First",color = '#42B300') # First set of data 
plt.bar(x2,y2,label = "Second",color = '#94E413') # Second set of data 
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.title ('$Bar $ $ Chart$')
plt.legend()
plt.show()

# Horizontal Bar Chart
Age = [28,33,43,45,57]
Name = ["Asif", "Steve", 'John', "Ravi", "Basit"] 
plt.barh(Name,Age, color ="yellowgreen")
plt.show()


# Changing the width of Bars
num1 = np.array([1,3,5,7,9])
num2 = np.array([2,4,6,8,10])
plt.figure(figsize=(8,4))
plt.bar(num1, num1**2, width=0.5 , color = '#FF6F00')
plt.bar(num2, num2**2, width=0.5 , color = '#FFB300')
plt.plot()
plt.show()

# Displaying values at the top of vertical bars
num1 = np.array([1,3,5,7,9])
num2 = np.array([2,4,6,8,10])
plt.figure(figsize=(10,6))
plt.bar(num1, num1**2, width=0.5 , color = '#FF6F00')
plt.bar(num2, num2**2, width=0.5 , color = '#FFB300') 
for x,y in zip(num1,num1**2):
    plt.text(x, y+0.05, '%d' % y, ha='center' , va= 'bottom') 
for x,y in zip(num2,num2**2):
     plt.text(x, y+0.05, '%d' % y, ha='center' , va= 'bottom')
plt.show()