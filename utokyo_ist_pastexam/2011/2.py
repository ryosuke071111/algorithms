f=open("c1.txt")
c1=list(f)

f=open("c2.txt")
c2=list(f)

compression = ["0","1","2","3","4","5","6","7","8","9","a"," ",",","."]

def count(f):
  count=0
  i=0
  while i+2<=len(f[0]):
    if f[0][i] in compression:
      if f[0][i+1] in compression and f[0][i+2] in compression:
        count+=1
        i+=2
    i+=1
  return count

print("c1.txtの圧縮文字列の数",count(c1))
print("c2.txtの圧縮文字列の数",count(c2))
