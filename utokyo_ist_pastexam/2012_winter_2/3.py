import matplotlib.pyplot as plt
import numpy as np
def f(x):
  return 0.5*x+10
a=[i for i in range(1,31)]
b=list(map(lambda x:f(x),a))
plt.plot(a,b,"bo")
plt.show()
