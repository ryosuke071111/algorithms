a,b,c,k = map(int,input().split())
s,t = map(int,input().split())

sums = a*s + b*t
if s+t >= k:
  sums = sums- (s+t)*c
print(sums)
