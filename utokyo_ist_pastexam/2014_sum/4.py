import math
ans=[]
def koch(d, p2, p3):
  global ans
  global n

  if d == 0:
    ans.append(p2*p3/2)
  elif d==1:
    ans.append(p2*p3/2*3)
  else:
    ans.append(p2*p3/2*4**(d-1)*3)
  if d==n:
    return
  p2=p2/3
  p3=p2*math.sqrt(3)/2
  koch(d+1,p2,p3)

n = int(input())
koch(0,10,5*math.sqrt(3))
print(sum(ans))


#簡単な答え
# import math
# l = 3
# ss = 10 * 5 * math.sqrt(3) /2

# n = int(input('-->'))
# s = ss
# for i in range(n):
#     ss = ss / (3**2)
#     s = s + ss * l
#     l = 4 * l

# print('K({0}) = {1}'.format(n,s))
