# n =  int(input())
# a = 0

# if n <= 0 or 1000 <= n:
#   exit()
# list1 = list(map(int, input().split()))
# #i = 0の時はエラーが出る
# for i in range(n-1, 0, -1):
#   j = i
#   while (j < n) and (list1[j] < list1[j-1]):
#     tmp = list1[j-1]
#     list1[j-1] =  list1[j]
#     list1[j] = tmp
#     j += 1
#     a += 1
# print(' '.join(map(str, list1)))
# print(a)

#ptn2
import numpy as np
np.random.seed(5)
ls= np.random.randint(1, 100, 10)
print(ls)
for i in range(10,0,-1):
  j=i
  while j<len(ls) and ls[j-1]>ls[j]:
    tmp=ls[j-1]
    ls[j-1]=ls[j]
    ls[j]=tmp
    j+=1

print(ls)
