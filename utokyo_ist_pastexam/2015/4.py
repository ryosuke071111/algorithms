# with open('program.txt') as f:
#   a = f.read().split("\n")
#   count={}
#   for i in a:
#     if i not in count:
#       count[i]=1
#     else:
#       count[i]+=1
#   cnt=0
#   for i,v in zip(count.keys(),count.values()):
#     if v >=2:
#       print(i)
#       cnt+=1
#   print("重複行の総数：",cnt)

#改造版（遊び）重複した行を文字の横に記載する　それの合計が奇数なら"hey"出力
with open('program.txt') as f:
  a = f.read().split("\n")
  count={}
  lines={}
  tmp=[]
  for i,v in enumerate(a):
    tmp.append([i,v])
  #同じキーのものがあれば、バリューを横に並べていく
  for k,v in tmp:
    lines.setdefault(v,[]).append(k)

  cnt0=0
  cnt1=0
  print('出現した行数の合計が奇数の場合のみに表示する')
  for i,v in zip(lines.keys(),lines.values()):
    if len(v)>=2:
      if sum(v)%2:
        print(i,v,'hey!')
        cnt0=max(len(i),cnt0)
        cnt1=max(len(str(v)),cnt1)
  print()
  print('文字の長さを揃える')
  for i,v in zip(lines.keys(),lines.values()):
    if len(v)>=2:
      print(str(i)+" "*(cnt0-len(str(i))+1)+str(v)+" "*(cnt1-len(str(v))+1)+"hey!")


  # for i in a:
  #   if i not in count:
  #     count[i]=1
  #     lines.append([i])
  #   else:
  #     count[i]+=1
  #     lines[]




  # cnt=0
  # for i,v in zip(count.keys(),count.values()):
  #   if v >=2:
  #     print(i)
  #     cnt+=1
  # print("重複行の総数：",cnt)

# 短い答え
# f = open("program.txt")
# l = f.read().split('\n')

# r = []
# for i,ll in enumerate(l):
#     if( (ll in l[:i] or ll in l[i+1:]) and ll not in r):
#         r.append(ll)

# print(len(r))
# for rr in r:
#     print(rr)
