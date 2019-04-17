from collections import Counter
n=int(input())
S=Counter([input() for i in range(n)]).most_common()
print(S[0][0])
