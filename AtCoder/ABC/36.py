n=int(input())
area=[]
for i in range(n):
  area.append(input())

ans=[[0 for i in range(n)] for i in range(n)]

for i in range(n):
  for j in range(n):
    ans[j][i]=area[i][j]

for i in ans:
  print("".join(i[::-1]))
