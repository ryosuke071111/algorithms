n=int(input())
P=[int(input()) for i in range(n)]
P.sort(reverse=True)
print(sum(P)-P[0]//2)
