n=int(input())
A=list(input().split())
print(" ".join(A[::-2]+A[n%2::2]))


