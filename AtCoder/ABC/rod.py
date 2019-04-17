ps = [1,5,8,9,10,17,17,20,24,30,1,5,8,9,10,17,17,20,24,30,1,5,8,9,10,17,17,20,24,30]
memo={}
memo[0]=0
def cut_rod(p,n):
  if n == 0:
    return 0
  q = 0
  for i in range(1,n):
    if i not in memo:
      q = max(q,ps[i]+cut_rod(ps,n-i))
    memo[n] = q
  return q


for i in range(10,1000500,10):
  cut_rod(ps,i)

print(memo)
