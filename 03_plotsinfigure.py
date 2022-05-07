import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# Display multiple plots in one figure (1 row & 2 columns)
plt.figure(figsize=(14,6))
x =  np.linspace(0, 10, 100) 
y1 = np.sin(x) # Sine Graph 
y2 = np.cos(x) # cosine graph 
plt.subplot(1,2,1) 
plt.plot(x,y1) 
plt.subplot(1,2,2) 
plt.plot(x,y2)
plt.show()

# Display multiple plots in one figure (2 row & 1 columns)
plt.figure(figsize=(12,6))
x = np.linspace(0, 10, 100)
y1 = np.sin(x) # Sine Graph
y2 = np.cos(x) # cosine graph
plt.subplot(2,1,1)
plt.plot(x,y1, "b-")
plt.subplot(2,1,2)
plt.plot(x,y2, "r-")
plt.tight_layout()
plt.show()


# # Display multiple plots in one figure using subplots()
x = np.arange(-50,50)
y1 = np.power(x,2)
y2 = np.power(x,3)
y3 = np.sin(x)
y4 = np.cos(x)
y5 = np.tan(x)
y6 = np.tanh(x)
y7 = np.sinh(x)
y8 = np.cosh(x)
y9 = np.exp(x)
fig1 , ax1 = plt.subplots(nrows=3,ncols=3 , figsize = (20,20)) # Create a figure and subplot
ax1[0,0].plot(x,y1,"tab:blue") # set the color of the line chart
ax1[0,0].set_title("Square Function") # setting title of subplot
ax1[0,0].set_xlabel(r'$X$' , fontsize = 14) #Set the label for the x-axis
ax1[0,0].set_ylabel(r'$Y$' , fontsize = 14) #Set the label for the y-axis
ax1[0,1].plot(x,y2,"tab:orange")
ax1[0,1].set_title("Cubic Function")
ax1[0,1].set_xlabel(r'$X$' , fontsize = 14)
ax1[0,1].set_ylabel(r'$Y$' , fontsize = 14)
ax1[0,2].plot(x,y3,"tab:green")
ax1[0,2].set_title("Sine Function")
ax1[0,2].set_xlabel(r'$X$' , fontsize = 14)
ax1[0,2].set_ylabel(r'$Y$' , fontsize = 14)
ax1[1,0].plot(x,y4,"b-")
ax1[1,0].set_title("Cosine Function")
ax1[1,0].set_xlabel(r'$X$' , fontsize = 14)
ax1[1,0].set_ylabel(r'$Y$' , fontsize = 14)
ax1[1,1].plot(x,y5,"r-") 
ax1[1,1].set_title("Tangent Function") 
ax1[1,1].set_xlabel(r'$X$' , fontsize = 14)
ax1[1,1].set_ylabel(r'$Y$' , fontsize = 14)
ax1[1,2].plot(x,y6,"g-")
ax1[1,2].set_title("Hyperbolic Tangent")
ax1[1,2].set_xlabel(r'$X$' , fontsize = 14)
ax1[1,2].set_ylabel(r'$Y$' , fontsize = 14)
ax1[2,0].plot(x,y7,"m-")
ax1[2,0].set_title("Hyperbolic Sine")
ax1[2,0].set_xlabel(r'$X$' , fontsize = 14) 
ax1[2,0].set_ylabel(r'$Y$' , fontsize = 14)
ax1[2,1].plot(x,y8,"y-") 
ax1[2,1].set_title("Hyperbolic Cosine")
ax1[2,1].set_xlabel(r'$X$' , fontsize = 14)
ax1[2,1].set_ylabel(r'$Y$' , fontsize = 14)
ax1[2,2].plot(x,y9,"k-")
ax1[2,2].set_title("Exponential Function")
ax1[2,2].set_xlabel(r'$X$' , fontsize = 18)
ax1[2,2].set_ylabel(r'$Y$' , fontsize = 18)

plt.show()

y = [[1,2,3,4,5] , [10,20,30,40,50],[60,70,80,90,100] ] 
cnt =0
plt.figure(figsize=(10,6))
for i in y:
    x1 = [10,20,30,40,50]
    cnt +=1
    print ('iteration Number :- {}'.format(cnt))
    print ('X1 Value :- {}'.format(x1))
    print('Y value (i) :- {}'.format(i)) 
    plt.plot(x1,i)
plt.show()