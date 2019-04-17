#8:05-
s=list(input())
w=[i for i in range(len(s)) if s[i]=="W"]
ideal=[j for j in range(s.count('W'))]
print(sum([i-j for i,j in zip(w,ideal)]))

