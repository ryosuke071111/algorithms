s = input()
n =int(input())
s = sorted(list(''.join(s)))
adana = []

for i in range(len(s)):
  for j in range(len(s)):
    adana.append(s[i]+s[j])

print(adana[n-1])

