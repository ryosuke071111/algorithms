# 9:28-
from collections import Counter
n=int(input())
dics=([Counter(input()) for i in range(n)])
std_dic=dics[0]

for dic in dics[1:]:
  for k,v in std_dic.items():
    if k in dic:
      std_dic[k]=min(v,dic[k])
    else:
      std_dic[k]=0
ans="".join(sorted(std_dic.elements()))
print(ans)

