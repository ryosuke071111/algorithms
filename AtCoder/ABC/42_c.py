#11:05-
n,k=map(int,input().split())
D=list(map(int,input().split()))
nums=[i for i in range(10) if i not in D]

def str_check(string):
  string=str(string)
  for i in string:
    if int(i) not in nums:
      return False
  return True

for i in range(n,100000):
  if str_check(i)==True:
    print(i)
    exit()
