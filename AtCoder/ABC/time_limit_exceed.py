N,T=map(int,input().split())
paths=[]
for i in range(N):
  c,t=map(int,input().split())
  paths.append([c,t])

s_path=float('inf')

for i in paths:
  if i[1]<=T:
    s_path=min(s_path,i[0])

if s_path == float('inf'):
  print('TLE')
else:
  print(s_path)


