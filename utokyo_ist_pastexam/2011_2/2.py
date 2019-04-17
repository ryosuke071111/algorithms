f1=open('c1.txt')
f1=f1.read().strip('\n')
f2=open('c2.txt')
f2=f2.read().strip('\n')
nums=[str(i) for i in range(10)]
def count(f):
  ans=0
  i=0
  while i<len(f):
    if f[i] in nums:
      ans+=1
      i+=3
    else:
      i+=1
  return ans
print("f1の中に含まれる置換指定文字列の数は:",count(f1))
print("f2の中に含まれる置換指定文字列の数は:",count(f2))
