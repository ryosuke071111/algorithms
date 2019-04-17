a = int(input())
b = int(input())
n = int(input())

flag =1
while flag:
  if n % a == 0 and n % b ==0:
    print(n)
    flag = 0
    break
  n += 1
