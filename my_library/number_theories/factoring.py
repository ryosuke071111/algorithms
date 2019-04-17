#素因数分解
def prime_factors(n):
  i = 2
  factors = []
  while i * i <= n:
    if n % i==0:
      n //= i
      factors.append(i)
    else:
      i += 1
  if n > 1:
    factors.append(n)
  return factors

#約数列挙
def make_divisors(n):
  divisors = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n//i)
  return sorted(divisors)
