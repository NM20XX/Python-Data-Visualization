from random import choice

#class to generate random walk
class RandomWalk():

  #initialize walks
  def __init__ (self, num_points = 3000):

    self.num_points = num_points

    #walk starts at 0,0
    self.x_values = [0]
    self.y_values = [0]

  #calculate all the points in the walk
  def fill_walk (self):

    #run till the walk reaches the desired length
    while len(self.x_values) < self.num_points:

      #decide which direction to go and how far to go in that direction
      x_direction = choice([1, -1])
      x_distance = choice([0,1,2,3,4])
      x_step = x_direction * x_distance

      y_direction = choice([1, -1])
      y_distance = choice([0,1,2,3,4])
      y_step = y_direction * y_distance

      #rejects move that go nowhere
      if x_step == 0 and y_step == 0:
        continue

      #calculate the next x and y values
      next_x = self.x_values[-1] + x_step
      next_y = self.y_values[-1] + y_step

      self.x_values.append(next_x)
      self.y_values.append(next_y)


#plotting the random walk
import matplotlib.pyplot as plt

#generating multiple random walks with 50000 points

while True:
  rw = RandomWalk(50000)
  rw.fill_walk()
  
  plt.figure(figsize=(10,6)) 
  #figure() function controls the width, height, resolution and background color of the plot
  #figsize takes a tuple, which decides the dimentions of the plotting window in inches
  
  point_numbers = list(range(rw.num_points))
  plt.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolor = 'none',  s = 1)
  
  #emphasize the first and last points
  plt.scatter(0, 0, c = 'green', edgecolor = 'none',  s = 100)
  plt.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolor = 'none',  s = 100)
  
  #remove the axes
  plt.axes().get_xaxis().set_visible(False)
  plt.axes().get_yaxis().set_visible(False)

  plt.show()
  
  again = input("Want to generate another walk? (y/n): ")
  if again.upper() == 'N':
    break
