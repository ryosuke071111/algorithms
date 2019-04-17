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

n = 2
koch(0,10,5*math.sqrt(3))
print(sum(ans))



