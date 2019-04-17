s=input()
n=int(input())
for i in range(n):
  l,r=map(int,input().split())
  a=s[l-1:r]
  s=s[:l-1]+a[::-1]+s[r:]
print(s)

