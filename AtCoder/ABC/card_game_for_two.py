n=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
print(sum(A[::2])-sum(A[1::2]))
