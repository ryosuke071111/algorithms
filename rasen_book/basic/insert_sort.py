import numpy as np
np.random.seed(0)

# n =  int(input())

# if n <= 0 or 1000 <= n:
#   exit()
# list1 = np.random.randint(1, 100, n)

# #i = 0の時はエラーが出る
# for i in range(1, len(list1)):
#   j = i
#   while (j>0) and (list1[j] < list1[j-1]):
#     tmp = list1[j-1]
#     list1[j-1] =  list1[j]
#     list1[j] = tmp
#     j -= 1
#   print(' '.join(map(str, list1)))
ls= np.random.randint(1, 100, 10)
print(ls)

for j in range(1,10):
  i=j-1
  key=ls[j]
  while i >0 and ls[i]>key:
    ls[i+1]=ls[i]
    i-=1
  ls[i+1]=key

print(ls)
