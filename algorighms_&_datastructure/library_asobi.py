import numpy as np
import matplotlib.pyplot as plt
x = np.array([[1,2],[4,4]])
y = np.array([[13,244],[444,44]])
# print(x.dot(x))
# print(x.dot(y))
# print(np.dot(x,x))
# print(np.dot(x,y))

row_1 = x[1,:]
row_2 = [1,3]

print(row_1)
print(row_2)

plt.plot(row_1, row_2)

plt.xlabel("aaa")
plt.ylabel("eee")
plt.title("title deesu")
plt.legend(["row_1","row_2"])
plt.show()
