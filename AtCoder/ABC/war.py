n,m = map(int,input().split())
a= []
b = []
count = 0
for i in range(m):
  a,b = map(int,input().split())
  a.append(a)
  b.append(b)

a = sorted(a)
b = sorted(b)

# for i in a:
#   for j in b:
#     if i < j:


print(a)
print(b)
