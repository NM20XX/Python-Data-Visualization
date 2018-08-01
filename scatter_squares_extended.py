#Calculating data automatically

import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [i*i for i in x_values]

plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor = 'none', s = 20) 
#edgecolor = 'none' is used to remove the outlines around points
#cmap argument to indicate which colormap to use.


#Title and label axes
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of value", fontsize = 14)

#Set size of tick labels
plt.tick_params(axis ='both', labelsize =14)

#Set the range for each axis
plt.axis([0,1100,0,1100000])

plt.show()

