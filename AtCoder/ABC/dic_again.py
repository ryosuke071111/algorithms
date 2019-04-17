#人の答え
N, K = map(int, input().split())
S = input()
ideal = sorted(S)
T = ''

for i in range(N):
    for j in range(len(ideal)):
        if S[i] == ideal[j]:
            T += ideal[j]
            del ideal[j]
            break
        A = 1
        mirror = list(ideal)
        del mirror[j]
        for k in range(i+1, N):
            if S[k] in mirror:
                mirror.remove(S[k])
            else:
                A += 1
        if K >= A:
            T += ideal[j]
            del ideal[j]
            K -= 1
            break

print(T)


#自分の答え

n,k=map(int,input().split())
s=list(input())
s=list("".join(s))
if k == len(s):
  print("".join(sorted(s)))
  exit()

index={s[i]:s.index(s[i]) for i in range(len(s))}


count=0
for i in range(len(s)):
  sml=s.index(min(s[i:]))
  if i!=sml and count+1 < k:
    count+=2
    s[i],s[sml]=s[sml],s[i]
    if s.index(s[sml]) == index[s[sml]]:
      count -= 1

print("".join(s))
