n,q=map(int,input().split())
counter=[0]* (n+1)
for i in range(q):
  l,r=map(int,input().split())
  counter[l]+=1
  if r+1<=n:
    counter[r+1]-=1

for i in range(1,n+1):
  counter[i]+=counter[i-1]
  print(counter)
  counter[i] = counter[i]%2
  print(counter)
  print("------------------")
print("".join(map(str,counter[1:])))

#セグメント木
#BIT
#いもす法
# [0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, -1]
[0, 1, 1, 0, 0, -1]
[0, 1, 1, 1, -1, -1]
[0, 2, 1, 1, -1, -1]
