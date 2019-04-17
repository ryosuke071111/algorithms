n,r=map(int,input().split())
deck=[i for i in range(n,0,-1)]
for i in range(r):
  p,c=map(int,input().split())
  deck=deck[p:p+c+1]+deck[:p+1]+deck[p+c+1:]
print(deck[0])
