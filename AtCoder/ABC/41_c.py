#11:57-
n=int(input())
A=list(map(int,input().split()))
dic={A[i]:i+1 for i in range(len(A))}
A.sort(reverse=True)
for i in A:
  print(dic[i])
