m=int(input())
ans=[]
for i in range(m):
  train=input()
  index=len(train)
  count=0
  tmp_a=set([])
  for i in range(1,index):
    tmp_a.add(train[:i]+train[i:])
    tmp_a.add(train[i:]+train[:i])
    tmp_a.add(train[:i][::-1]+train[i:])
    tmp_a.add(train[i:][::-1]+train[:i])
    tmp_a.add(train[:i]+train[i:][::-1])
    tmp_a.add(train[i:]+train[:i][::-1])
    tmp_a.add(train[:i][::-1]+train[i:][::-1])
    tmp_a.add(train[i:][::-1]+train[:i][::-1])
  ans.append(len(tmp_a))
for i in ans:
  print(i)




