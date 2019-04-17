def is_prime(x):
  if x == 1:
    return False
  for i in range(2, x):
    if x % i == 0:
      return False
    if i * i>= x:
      break         #ある数で割ったときに0でないならその二乗で割った数も0でないから計算する必要ない。
  return True

def check(l,r):
  count = 0
  for i in range(l,r+1,2):
    if is_prime(i) == True:
      if is_prime((i+1)//2) == True:
        sim_2017[i] += 1
  return count


Q = int(input())

sim_2017 = [0]*(10**5+1)

nums = []
for i in range(Q):
  l,r = map(int,input().split())
  nums.append(check(l,r))


for i in nums:
  print(i)


#誰かの回答
NMAX = 10**5+1

is_prime = [True]*NMAX
for i in range(2, NMAX):
    if is_prime[i]:
        for j in range(2*i, NMAX, i):
            is_prime[j] = False

sim_2017 = [0]*NMAX
for i in range(3, NMAX, 2):
    if is_prime[i] and is_prime[(i+1)//2]:
        sim_2017[i] += 1
for i in range(1, NMAX):
    sim_2017[i] += sim_2017[i-1]

q = int(input())
for _ in range(q):
    l, r = list(map(int, input().split()))
    ans = sim_2017[r] - sim_2017[l-1]
    print(ans)

