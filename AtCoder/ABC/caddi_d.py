n=int(input())
A=[int(input()) for i in range(n)]
for i in A:
  if i%2==1:
    print('first')
    exit()
print('second')

