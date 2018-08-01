#Plotting a series of points with scatter

#Python 3.7.0
#matplotlib is a tool, mathematical plotting library
#pyplot is a module

#pip install matplotlib

import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]

plt.scatter(x_values,y_values, s = 100)

#Title and label axes
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of value", fontsize = 14)

#Set size of tick labels
plt.tick_params(axis ='both', labelsize = 14)

plt.show()