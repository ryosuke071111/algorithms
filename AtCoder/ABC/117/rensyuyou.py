# n,k=map(int,input().split())
# A=list(map(int,input().split()))
# bit_max=40
# ans=0
# for i in range(bit_max,-1,-1):
#   Xi=1<<i
#   ck= len([1 for a in A if Xi&a!=0])
#   tmp=ck
#   if Xi<=k and tmp<n-ck:
#     tmp=n-ck
#     k-=tmp
#   contribution=Xi*tmp
#   ans+=contribution
# print(ans)

# def is_even(n):
#   """
#   >>> is_even(10)
#   True
#   >>> is_even(11)
#   False
#   """
#   return n % 2 == 0


def is_odd(n):
  """
  >>> is_odd(9)
  False
  """
  return n%2== 1

import doctest
doctest.testmod()
