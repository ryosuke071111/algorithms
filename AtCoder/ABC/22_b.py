from collections import Counter
n=int(input())
A=Counter([int(input()) for i in range(n)])
print(sum(list(A.values()))-len(A))
