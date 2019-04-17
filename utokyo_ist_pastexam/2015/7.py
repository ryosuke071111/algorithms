f=open('program1.txt')
a=f.read().split('\n')
tmp_ls=[]
tmp=""
for i in a:
  if tmp==i:
    tmp_ls.append(i)
    if len(tmp_ls)>=4:
      print(*tmp_ls,sep="\n")
      tmp_ls=[]
  else:
    tmp_ls=[i]
  tmp=i


