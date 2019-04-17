from collections import Counter
n=int(input())
D=[int(input()) for i in range(n)]
D=Counter(D)
print(len(D))
