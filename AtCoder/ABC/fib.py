# # #メモ化 #1
fib_memo={}

def fib(n):
  if n < 3:
    return 1
  if n not in fib_memo:
    fib_memo[n] = fib(n-1) + fib(n-2)
  return fib_memo[n]

print(fib(999))



# counter = 0

# #メモ化 #2
# def fib(n):
#   global counter
#   counter += 1
#   if n in [0,1]:
#     return 1
#   return fib(n-1)+fib(n-2)

# print(fib(240))
# print(counter,"回の呼び出し")

# #キャッシュを使うver
# from functools import lru_cache

# @lru_cache()
# def fib(n):
#   if n < 3:
#     return 1
#   return fib(n-1)+fib(n-2)

# print(fib(100))


# #数式バージョン
# def fib(n):
#   f =((1+5**0.5)/2)**n / 5** 0.5 + 0.5
#   return int(f)
# print(fib(1000))


#行列バージョン
def mat_mul(a,b):
  z=[[0,0],
     [0,0]]
  for i in range(2):
    for j in range(2):
      for k in range(2):
        z[i][j]+=a[i][k]*b[k][j]
  return z

def mat_pow(x,n):
  if n ==0:
    return [[1,0],
            [0,1]]
  elif n%2:
    return mat_mul(x,mat_pow(x,n-1))
  else:
    half_pow = mat_pow(x,n/2)
    return mat_mul(half_pow,half_pow)

def fib(n):
  if n==0:
    return 0
  else:
    f =[[0,1],
        [1,1]]
    return mat_pow(f,n-1)[1][1]
print(fib(50))
