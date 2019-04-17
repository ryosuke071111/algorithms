import matplotlib.pyplot as plt
import math as mp
import numpy as np


x =np.linspace(0,5, num=1000)
frequency = 40
unit_time = 1/30

def exponential_dist(lamda, x):
  y = lamda * np.exp(-lamda * x)
  # y = round(a, 5)
  return y

def draw_graph(x, y, title):
  plt.title(title)
  plt.plot(x, y, linestyle='-')
  plt.show()


draw_graph(x, exponential_dist(frequency, x), "exponential_dist" )

