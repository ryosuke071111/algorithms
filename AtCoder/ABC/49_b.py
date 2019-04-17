h,w=map(int,input().split())
C=[""]*(2*h)
for i in range(0,h*2,2):
  C[i]=input()
  if i+1 <=len(C):
    C[i+1]=C[i]
for i in C:
  print(i)



