n,m=map(int,input().split())
A=[input() for i in range(n)]
B=[input() for i in range(m)]

for i in range(n):
  for j in range(n):
    k=j+m
    if k <= n:
      if A[i][j:k]== B[0]:
        o=1
        for l in range(i+1,i+m):
          if l<n:
            if A[l][j:k]!=B[o]:
              break
            else:
              o+=1
        if o==m:
          print('Yes')
          exit()
print('No')

