a=[int(input())]
def f(n):
  if n%2==1:
    return 3*n+1
  else:
    return n//2
for i in range(1,1000000):
  tmp=f(a[i-1])
  if tmp in a:
    print(i+1)
    exit()
  else:
    a.append(tmp)
