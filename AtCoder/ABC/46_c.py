#7:40-
n=int(input())
a=b=1
for i in range(n):
  x,y=map(int,input().split())
  m=max((a-1)//x+1,(b-1)//y+1) #天井関数(x以上の最小の整数)<=>床関数（x以下の最大の整数）
  a=m*x
  b=m*y
print(a+b)

