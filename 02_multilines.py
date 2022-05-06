import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

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


#Plotting multiple sets of data

x = np.linspace(0, 10, 2000)
plt.figure(figsize=(10,6))
plt.plot(x,np.sin(x) , label = '$Sin(X)$')
plt.plot(x,np.cos(x) , label = '$cos(X)$')
plt.xlabel(r'$X$' , fontsize = 18)
plt.ylabel(r'$Y$' , fontsize = 18)
plt.title("$Sin(x) $ $ & $ $ Cos(x)$" ,fontsize = 14)
plt.legend(loc = 'upper right') # Legend will be placed at upper right position
plt.show()

#Changing the line style

plt.figure(figsize=(10,5))
x = np.array([1,2,3,4,5,6])
y1 = np.power(x,2)
y2 = np.power(x,3)
plt.plot(x,y1, "b-" , label = '$y1 = x^2$') # Setting up legends
plt.plot(x, y2,color='red',linewidth=1.0,linestyle='--') # Setting up legends plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.legend(loc='upper center', fontsize='large')
plt.show()

# Line Styling
x = np.linspace(0, 10, 2000)
plt.figure(figsize=(16, 9))
plt.plot(x,np.sin(x) , label = '$Sin(X) $ $ Dashed $' , 
         linestyle='dashed') plt.plot(x+1,np.sin(x) ,
        label = '$Sin(X) $ $ Dashdot $' , 
        linestyle='dashdot') plt.plot(x,np.cos(x) , label = '$cos(X) $ $ Solid $' , linestyle='solid') plt.plot(x+1,np.cos(x) , label = '$cos(X)$ $ Dotted $' , linestyle='dotted') plt.xlabel(r'$X$' , fontsize = 18)
plt.ylabel(r'$Y$' , fontsize = 18)
plt.title("$Sin(x) $ $ & $ $ Cos(x)$" ,fontsize = 14)
plt.legend(loc = 'upper right' , fontsize = 14 , bbox_to_anchor=(1.2, 1.0)) # Legend will b plt.show()