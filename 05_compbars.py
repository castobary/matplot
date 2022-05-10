import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# Barplots with -y and +y axes
x = np.arange(1,21)
plt.figure(figsize=(16,8))
y1 = np.random.uniform(0.1,0.7,20)
y2 = np.random.uniform(0.1,0.7,20)
plt.bar(x, +y1, facecolor='#C0CA33', edgecolor='white') #specify edgecolor by name 
plt.bar(x, -y2, facecolor='#FF9800', edgecolor='white')
for x,y in zip(x,y1):
    plt.text(x, y+0.05, '%.2f' % y, ha='center' , va= 'bottom', fontsize = 10)
plt.xlim(0,21)
plt.ylim(-1.25,+1.25)
plt.show()

# Stacked Vertical Bar
plt.style.use('seaborn-darkgrid')
x1= ['Cassandra','Cherly','Alice','Alex']
y1= [17,18,29,40]
y2 = [20,21,22,23]
plt.figure(figsize=(5,7))
plt.bar(x1,y1,label = "Open Tickets",width = 0.5,color = '#FF6F00')
plt.bar(x1,y2,label = "Closed Tickets",width = 0.5 ,bottom = y1 , color = '#FFB300')
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.title ('$Bar $ $ Chart$')
plt.legend()
plt.show()


plt.style.use('seaborn-darkgrid') 
x1= ['Cassandra','Cherly','Alice','Alex']
y1= np.array([17,18,29,40])
y2 =np.array([20,21,22,23])
y3 =np.array([5,9,11,12])
plt.figure(figsize=(5,7))
plt.bar(x1,y1,label = "Open Tickets",width = 0.5,color = '#FF6F00')
plt.bar(x1,y2,label = "Closed Tickets",width = 0.5 ,bottom = y1 , color = '#FFB300')
plt.bar(x1,y3,label = "Cancelled Tickets",width = 0.5 ,bottom = y1+y2 , color = '#F7DC6F')
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.title ('$Bar $ $ Chart$')
plt.legend()
plt.show()