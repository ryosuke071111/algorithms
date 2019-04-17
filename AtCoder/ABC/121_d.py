a,b=map(int,input().split())

# def f(n):
#   if n%4==0:
#     return n
#   elif n%4==1:
#     return 1
#   elif n%4==2:
#     return n+1
#   elif n%4==3:
#     return 0
# print((f(b)^f(a-1)))

def g(n):
  return int((n+1)/2 %2)

def f(n):
  if n%2==1:
    return g(n)
  else:
    return g(n+1)^(n+1)
print((f(b)^f(a-1)))

# a=0
# for i in range(17):
#   print(i, "0"*(4-len(bin(i)[2:]))+bin(i)[2:],"0"*(4-len(bin(a^i)[2:]))+bin(a^i)[2:])
#   a=a^i
