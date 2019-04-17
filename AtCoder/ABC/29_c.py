import itertools
n=int(input())
for i in itertools.product("abc",repeat=n):
  print(*i,sep="")

