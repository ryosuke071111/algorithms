n = int( input() )
if n ==1:
  print(0)
else:
  ls=[]
  for i in range(1,n):
    if i**2<=n:
      a = n%i
      b = n//i
      ls.append(abs(b-i)+a)
    else:
      break
  print(min(ls))

#TLE
# import math
# n=int(input())
# tmp0=int(math.sqrt(n))
# tmp1=tmp0
# ans=100000


# for i in range(int((tmp0*0.8)),int((tmp0*1.5))):
#   j=i
#   while i*j<=n:
#     if ans > abs(abs(j-i)+(n-i*j)):
#       ans = abs(abs(j-i)+(n-i*j))
#     j+=1
# print(ans)
