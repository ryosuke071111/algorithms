n,h,w=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(n)]
count=0
for a,b in AB:
  if a>=h and b>=w:
    count+=1
print(count)
