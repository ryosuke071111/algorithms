from collections import Counter
n=int(input())
S=[input() for i in range(n)]
S=dict(Counter(S).most_common())
m=int(input())
T=[input() for i in range(m)]
T=dict(Counter(T).most_common())

for i in S:
  for k in T:
    if i==k:
      S[i] -= T[k]

S=sorted(S.items(),key=lambda x:x[1],reverse=True)

if S[0][1] < 0:
  print(0)
else:
  print(S[0][1])

