# a,b,k = map(int,input().split())
# num=[]

# if b-a >= k:
#   for i in range(a,a+k):
#     num.append(i)
#   for i in range(b-k+1,b+1):
#     num.append(i)
# else:
#   for i in range(a,b+1):
#     num.append(i)

# for i in sorted(set(num)):
#   print(i)


#別解
a,b,k = map(int,input().split())
num=[i for i in range(a,b+1)]
for i in sorted(set(num[:k])|set(num[-k:])):
  print(i)

#
