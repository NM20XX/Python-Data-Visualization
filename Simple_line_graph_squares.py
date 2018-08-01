#Plotting a simple line graph

#Python 3.7.0
#matplotlib is a tool, mathematical plotting library
#pyplot is a module

#pip install matplotlib

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.plot(input_values, squares, linewidth = 5) #linewidth controls the thickness of the line that plot() generates.

#Title and label axes
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of value", fontsize = 14)

#Set size of tick labels
plt.tick_params(axis ='both', labelsize = 14)

plt.show()

