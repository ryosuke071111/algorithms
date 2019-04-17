n, a, b = map(int, input().split())
sumn = 0
tmp = 0

for i in range(n+1):
  for j in range((len(str(i)))):
    tmp += int(str(i)[j])
  if tmp >=a and tmp<= b:
      sumn += i
  tmp = 0

print(sumn)

#別解------------------------------------------
for i in range(n+1):
    if a <= sum(list(map(int,list(str(i))))) <= b:
        ans += i
