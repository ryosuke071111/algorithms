n = int(input())
# lr=[[0,0] for i in range(n)]
num=0

for i in range(n):
  a,b = map(int,input().split())
  num += b-a+1

print(num)
