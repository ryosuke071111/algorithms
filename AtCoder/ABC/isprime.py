import math
def is_prime(x):
  if x == 1:
    return False
  for i in range(2, x): #1と自分以外で割れるか徐々に検証している
    if x % i == 0:
      print("xiは",i)
      return False
    if i * i>= x:       #for 文を2乗で超えた時点で止める
      print('i*i',i*i,i)
      break         #breakにしないと膨大な数字をいつまでも追いかけている
  return True

n = int(input())
ans = 0
for i in range(n):
  x = int(input())
  if is_prime(x):
    ans += 1
print(ans)
