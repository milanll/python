import matplotlib.pyplot as plt #importing matplot lib library
import numpy as np 

x = range(100) 
#print x, print and check what is x
y =[val**2 for val in x] 
#print y
plt.plot(x,y) #plotting x and y
plt.show()