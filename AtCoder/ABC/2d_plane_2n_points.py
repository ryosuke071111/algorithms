n = int(input())

reds =[list(map(int,input().split())) for i in range(n)]
blues = [list(map(int,input().split())) for i in range(n)]
reds.sort(key=lambda x: x[1],reverse=True)
blues = sorted(blues)
count = 0

for i in reds:
  for j in blues:
    if i[0] < j[0] and i[1] < j[1]:
      count += 1
      blues.remove(j)
      break
print(count)

