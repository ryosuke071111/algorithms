n=int(input())
A=[0]+list(map(int,input().split()))+[0]
diff=[abs(A[i]-A[i-1]) for i in range(1,len(A))]
sums=sum(diff)

for i in range(1,n+1):
  # if i==n:
  #   print(sums-abs(A[i]-A[i+1])-abs(A[i-1]-A[i])+abs(A[i-1]-A[i+1]))
  #   exit()
  # elif A[i]<=A[i+1] and ((A[i]>0 and A[i+1]<0) or (A[i]<0 and A[i+1]>0)):
  #   print(sums-abs(A[i]-A[i+1])-abs(A[i-1]-A[i])+abs(A[i-1]-A[i+1]))
  # elif A[i]<=A[i+1]:
  #   print(sums)
  # else:
    print(sums-abs(A[i]-A[i+1])-abs(A[i-1]-A[i])+abs(A[i-1]-A[i+1]))

