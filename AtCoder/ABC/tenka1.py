N=int(input())
for h in range(1,3501):
  for n in range(1,3501):
    tmp=4*n*h-N*n-N*h
    if tmp>0:
      if N*h*n%tmp==0:
        print(h,n,N*h*n//tmp)
        exit()
