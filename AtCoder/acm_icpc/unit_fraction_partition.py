from functools import lru_cache
import pathlib


@lru_cache(maxsize=1<<10)

def solve(p,q,a,n):
  def _solve(num,dem,d,m,s):
    if num==0:
      return 1
    if d == 0:
      return 0
    if num * a //m < dem:
      return 0
    return sum((_solve(num*i-dem, dem*i, d-1, m*i, i) for i in range(s, min(dem*n//num, a//m)+1)),0)
  return _solve(p,q,n,1,1)
ans=[]


#新規ファイルを作成して書き込み
with open("nums.txt") as f:
  with open('output.txt', mode = 'w') as r:
    while True:
      p,q,a,n=map(int,f.readline().split())
      if p==0:
        break
      ans.append(solve(p,q,a,n))
    for i in ans:
      print("aaaa",file=r)
      # r.write(str(i))
      # r.write("\n")



