#10:04-
import math
n,k=map(int,input().split())
A=list(map(int,input().split()))
print(1 if n-k==0 else math.ceil((n-1)/(k-1)))

