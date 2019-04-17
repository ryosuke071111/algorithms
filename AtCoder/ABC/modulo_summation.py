n = int(input())
mods = list(map(int,input().split()))

m =1
for i in range(len(mods)):
  m *= mods[i]

sums = 0
for i in range(len(mods)):
  sums += (m-1) %mods[i]

print(sums)
