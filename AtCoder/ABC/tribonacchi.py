

#正解
# n=int(input())
# a,b,c=0,0,1
# for i in range(n-1):
#   tmp=a+b+c
#   a = b%10007
#   b = c%10007
#   c = tmp%10007
# print(a)

#最高速
n=int(input())-1
def matmul(a,b):
  ret = [[0 for j in range(3)] for i in range(3)]
  for i in range(3):
    for j in range(3):
      for k in range(3):
        ret[i][j] += a[i][k]*b[k][j]
        ret[i][j] %= 10007
  return ret

e = [[1,0,0],
     [0,1,0],
     [0,0,1]]
x = [[0,0,1],
     [1,0,1],
     [0,1,1]]
while n:
  if n%2:
    e = matmul(e,x)
  x = matmul(x,x)
  n = n//2
print(e[2][0])


# 間違い
# from functools import lru_cache
# memo={}
# n=int(input())

# @lru_cache()
# def tri(n):
#   if n < 3:
#     memo[n]=0
#   elif 2< n < 5:
#     memo[n]=1
#   if n not in memo:
#     memo[n]=tri(n-3)+tri(n-2)+tri(n-1)
#   return memo[n]

# if n > 800:
#   for i in range((n//100)+1):
#     tri(100*i)
# print(tri(n)%10007)



