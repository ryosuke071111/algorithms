a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0

dp = [[[-1 for i in range(a+1)] for i in range(b+1)] for i in range(c+1)]

for i in range (c+1):
  for j in range(b+1):
    for k in range(a+1):
      dp[i][j][k] = x - (50*i+100*j+k*500)
      if dp[i][j][k] == 0:
        count += 1
print(count)

#メモリに登録する必要ない
#単純にループを回して該当する値があったらカウントを追加するだけでよかった
