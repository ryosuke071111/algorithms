# #間違いコード
# prime = []

# def isPrime(x):
#   if x <= 1:
#     return False
#   for i in range(2, x):
#     if x % i ==0:
#       return False
#   prime.append(x)

# N = int(input())

# for i in range(N):
#   num = int(input())
#   isPrime(num)

# print(len(prime))


#正解コード
def is_prime(x):
  if x == 2:
    return True
  if x < 2 or x % 2 == 0:
    return False
  for i in range(3, int(x**0.5)+1, 2):
    if x % i == 0:
      return False
  return True

N = int(input())
cnt = 0
for _ in range(N):
  i = int(input())
  cnt += is_prime(i)

print(cnt)
