n = int(input())
t,a = map(int,input().split())
temp = list(map(int,input().split()))
tmp = 10**9
index= 1

for i in temp:
  if abs(a- (tmp)) > abs(a- (t - i * 0.006)):
    tmp = t - i * 0.006
    index = temp.index(i)+1


print(index)
