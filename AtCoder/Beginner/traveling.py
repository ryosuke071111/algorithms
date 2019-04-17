# n = int(input())
# for i in range(n):
#   t,x,y = map(int,input().split())
#   if x + y > t or (x+y+t)%2:
#     print('No')
#     exit()
# print('Yes')


#別解(pythonのリストは初期値を入れないとt[i]で指定して値を入れられない)
n = int(input())
t = [0]+[0 for i in range(n)]
x = [0]+[0 for i in range(n)]
y = [0]+[0 for i in range(n)]

for i in range(1, n+1):
  t[i],x[i], y[i] = map(int,input().split())

for i in range(n):
  dt = t[i+1] - t[i]
  dist = abs(x[i+1] - x[i]) + abs(y[i+1] - y[i])
  if dist > dt:
    print('No')
    exit()
  if dist % 2 != dt %2:
    print('No')
    exit()
print('Yes')
