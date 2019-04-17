f=open('mat1.txt')
a=f.read().split("\n")[:-1]
a=a[0].split(',')
a=list(map(lambda x:x.split(),a))
print("行:",len(a),"列数:",len(a[0]))
