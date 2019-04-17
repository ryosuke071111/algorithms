n,s,t = map(int,input().split())
w = [0 for i in range(n)]
w[0] = int(input())
A =[0 for i in range(n)]
best_body=0
if s <= w[0] and w[0] <=t:
  best_body += 1

for i in range(1, n):
  A[i] = int(input())
  w[i] = w[i-1] + A[i]
  if s <= w[i] and w[i] <=t:
    best_body += 1

print(best_body)


#別解
n,s,t = map(int,input().split())
w = 0
count = 0

for i in range(n):
  w += int(input())
  if s <= w <= t:
    count += 1
print(count)
