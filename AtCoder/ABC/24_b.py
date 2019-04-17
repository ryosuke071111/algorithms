n,t=map(int,input().split())
A=[int(input()) for i in range(n)]
time=0
for i in range(len(A)):
  if i < len(A)-1:
    if A[i+1]-A[i] > t:
      time+=t
    else:
      time+=A[i+1]-A[i]
print(time+t)
