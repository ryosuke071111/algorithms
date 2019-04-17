#8:46-
h,w=map(int,input().split())
ans=10**9
w1,w2=w//2,w-w//2
for i in range(1,h):
  s=i*w,w1*(h-i),w2*(h-i)
  ans=min(ans,max(s)-min(s))
  # print(s,ans)
h1,h2=h//2,h-h//2
for i in range(1,w):
  s=i*h,h1*(w-i),h2*(w-i)
  ans=min(ans,max(s)-min(s))
  # print(s,ans)
if h%3==0 or w%3==0:
  ans=0

#均等に取ると、縦か横の余分な文しか余らない
#自分の考え方であっているからそれを真剣に実装してみる根気が必要
if w >2:
  ans=min(ans,w)
if h >2:
  ans=min(ans,h)
print(ans)

