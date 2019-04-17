#普通に√x以下で素数探し
import math
def is_prime(x):
  if x == 1:
    return False
  for i in range(2, x):
    if x % i == 0:
      return False
    if i * i>= x:
      break         #ある数で割ったときに0でないならその二乗で割った数も0でないから計算する必要ない。
  return True

n = int(input())
ans = 0
for i in range(n):
  x = int(input())
  if is_prime(x):
    ans += 1
print(ans)

#エラストてネスの篩（ふるい）　O(nloglogn)
is_prime = [True]*NMAX
for i in range(2, NMAX):
    if is_prime[i]:
        for j in range(2*i, NMAX, i):
            is_prime[j] = False

#2で素数探索（倍数を削除）→3で素数探索（倍数を削除）→5で素数探索（倍数削除）


# Fermat's 小定理O(log(n!)
def is_prime(x):
    if x == 2:
        return 1
    elif x % 2 == 0:
        return 0
    else:
        return pow(2, x - 1, x) == 1

def is_prime(n):
  if n == 2:
    return 1
  elif n % 2 == 0:
    return 0
  else:
    return pow(2,n-1,n) == 1

import sys

def solve():
    file_input = sys.stdin
    N = file_input.readline()
    cnt = 0
    for n in map(int, file_input):
        cnt += is_prime(n)
    print(cnt)

solve()

