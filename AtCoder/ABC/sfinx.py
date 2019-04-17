# n,m = map(int,input().split())

# for i in range(1, n+1):
#   for j in range(1, n-i+1):
#     k = n-i-j
#     if 2*i + 3*j + 4*k ==m:
#       print(i,j,k,"\n")
#       exit()

# print(-1,-1,-1)

n,m = map(int,input().split())

for j in range(2): #老人
  for k in range(n+1-j): #ベイビー
    i = n-j-k #大人
    print(i,j,k)
    if (i*2+j*3+k*4) ==m:
        print(i,j,k)
        exit()
print(-1,-1,-1)
