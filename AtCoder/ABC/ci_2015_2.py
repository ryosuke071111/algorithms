# mod=2**24
# memo={}
# def f(n):
#   if n<1:
#     return 1
#   elif n not in memo:
#     memo[n]= (161*f(n-1)+2457)%mod
#   return memo[n]
# print(f(99))

# count=0
# for i in range(100):
#   if f(i)%2==0:
#     count+=1
# print("偶数の数は",count)

# count_odd=0
# for i in range(100):
#   if f(i)%2==1:
#     count_odd+=1
# print("奇数の数は",count_odd)

# for i in range(1000000+1):
#   f(i)
# print(memo[1000000])

# memo_g={}
# mod_1=2**26
# def g(n):
#   if n < 1:
#     return 1
#   elif n not in memo_g:
#     memo_g[n]=(1103515245*g(n-1)+12345)%mod_1
#   return memo_g[n]


#  #(6)の答え
# n=int(input())
# k=1
# ans=g(n)
# while True:
#   if(g(n+k)) ==ans:
#     break
#   k+=1
# print(memo_g[n])
# print(memo_g[n+k])


#(7)の答え
# mod_1=2**10
# def h(n):
#   return g(n)%mod_1
# k= 1
# n=int(input())
# ans=h(n)
# while True:
#   if h(n+k)==ans:
#     break
#   k+=1
# print(h(n+k))
# print(h(n))
# print(k)
# print(memo_g)

#②
# with open('txt_s.txt') as f:
#   a = str(f.readlines())       #行ごとに読み込んでリスト化
#   b = a
# a=a.replace('[',"").replace("]","").replace('\\n',"").replace('"',"").replace("'","").split(",")
# tmp=len(a[0].split())
# print("列数：",tmp,"行数：",b.count(",")+1)

# #③
# with open('txt_s.txt') as f:
#   a = str(f.readlines())       #行ごとに読み込んでリスト化
# a=a.replace('[',"").replace("]","").replace('\\n',"").replace('"',"").replace("'","").split(",")
# matrix=list(map(lambda x:x.split(),a))

# ans=0
# for i in range(b.count(",")+1):
#   for j in range(tmp):
#     if i ==j:
#       ans+=int(matrix[i][j])
#   print(matrix[i])
# print(ans)

#④
from collections import deque
n=3
m=3
cache=deque([]*5)
count=0
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[0]*m for i in range(n)]

for k in range(3):
  for i in range(n):
    for j in range(m):
        print(i,j,k)
        if A[i][k] not in cache:
          if len(cache)>=5:
            cache.popleft()
            cache.append(A[i][k])
          else:
            cache.append(A[i][k])
          count+=1
        else:
            cache.remove(A[i][k])
            cache.append(A[i][k])
        if A[k][j] not in cache:
          if len(cache)>=5:
            cache.popleft()
            cache.append(A[k][j])
          else:
            cache.append(A[k][j])
          count+=1
        else:
          cache.remove(A[k][j])
          cache.append(A[k][j])
        B[i][j]+=A[i][k]*A[k][j]
print(B)
print(cache)
print(count)

