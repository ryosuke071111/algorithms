# n,x=map(int,input().split())
# a,p=[1],[1]
# for i in range(n):
#   a.append(a[i]*2+3)
#   p.append(p[i]*2+1)

# def f(n,x):
#   if n==0:
#     return 0 if x<=0 else 1
#   elif x<= 1 + a[n-1]:
#     return f(n-1,x-1)
#   else:
#     return p[n-1]+1+f(n-1,x-2-a[n-1])


n,x = (int(i) for i in input().split())
def pc(n,k):
  if n and k==1: return 0
  elif k==1: return 1
  elif k<2**(n+1)-1: return pc(n-1,k-1)
  elif k==2**(n+1)-1: return 2**n
  elif k<2**(n+2)-3: return 2**n+pc(n-1,k-2**(n+1)+1)
  else: return 2**(n+1)-1
print(pc(n,x))
