from random import randint

#single die class
class Die():
  
  def __init__(self, num_sides = 6):
    self.num_sides = num_sides
	
  def roll(self):
    return randint(1, self.num_sides)
	
#------------------------------------------------------------------------------------	
#rolling a D6 multiple times and checking the results	
die = Die()

roll_list = []
for i in range(0,1000):
  roll_list.append(die.roll())
print(roll_list)

#------------------------------------------------------------------------------------
#analyzing the results by counting how many times we roll each number
freq = []
#list Comprehensionshon
[freq.append(roll_list.count(i)) for i in range(1,die.num_sides+1)]
  
print(freq)

#------------------------------------------------------------------------------------

#histogram

import pygal

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"

x_labels_list = []
#list Comprehensionshon
[x_labels_list.append(i) for i in range(1,die.num_sides+1)]
  
hist.x_labels = x_labels_list 
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', freq)
hist.render_to_file("die_data.svg")



#------------------------------------------------------------------------------------
#rolling two dice

die1 = Die()
die2 = Die()

roll_list = []
for i in range(0,1000):
  roll_list.append(die1.roll() + die2.roll())
print(roll_list)

#------------------------------------------------------------------------------------
#analyzing the results by counting how many times we roll each number
freq = []
#list Comprehensionshon
#die1.num_sides + die2.num_sides  is the largest possible output
max_sides = die1.num_sides + die2.num_sides 

[freq.append(roll_list.count(i)) for i in range(2,max_sides + 1)]
  
print(freq)

#------------------------------------------------------------------------------------

#histogram

import pygal

hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times"

x_labels_list = []
#list Comprehensionshon
[x_labels_list.append(i) for i in range(2,max_sides + 1)]
  
hist.x_labels = x_labels_list 
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', freq)
hist.render_to_file("dice_data.svg")