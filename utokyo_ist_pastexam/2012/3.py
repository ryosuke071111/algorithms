import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return 0.5*x+10

x=np.arange(0,30,0.001)
plt.plot(x, f(x))
plt.show()
