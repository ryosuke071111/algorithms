counts={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0}
S=input()
for i in S:
  counts[i]+=1
a=list(counts.values())
print(a[0],a[1],a[2],a[3],a[4],a[5])
