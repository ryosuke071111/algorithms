import itertools

n,m=map(int,input().split())
A=[input()for i in range(n)]
B=[input()for i in range(m)]


for i,j in itertools.product(range(n-m+1),repeat=2):
  if [_[j:j+m] for _ in A[i:i+m]] == B:
      print('Yes')
      exit()
print('No')

