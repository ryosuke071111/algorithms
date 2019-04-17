def f(x):
  if x==1:
    return 10
  if x==2:
    return 7
  if x==3:
    return 25
  if x==4:
    return 24

def constrain(x):
  if x==1:
    return 2
  if x==2:
    return 1
  if x==3:
    return 6
  if x==4:
    return 5

dp=[[[0,0] for i in range(7+1)] for i in range(4+1)]
for i in range(1,5):
  for j in range(1,8):
    if dp[i-1][j-constrain(i)][1]+constrain(i)<=j:
      max_n=dp[i][j-1][0]
      flag="a"
      if dp[i-1][j][0]>max_n:
        max_n=dp[i-1][j][0]
        flag="b"
      if dp[i-1][j-constrain(i)][0]+f(i)>max_n:
        max_n=dp[i-1][j-constrain(i)][0]+f(i)
        flag="c"
      dp[i][j][0]=max_n

      # max(dp[i-1][j][0],dp[i][j-1][0],dp[i-1][j-constrain(i)][0]+f(i))

      if flag=="c":
        dp[i][j][1]=dp[i][j-constrain(i)][1]+constrain(i)
      elif flag=="b":
        dp[i][j][1]=dp[i-1][j][1]
      else:
        dp[i][j][1]=dp[i][j-1][1]
    else:
      max_n=dp[i][j-1][0]
      flag="a"
      if dp[i-1][j][0]>max_n:
        max_n=dp[i-1][j][0]
        flag='b'
      dp[i][j][0]=max_n
      if flag=="b":
        dp[i][j][1]=dp[i-1][j][1]
      else:
        dp[i][j][1]=dp[i][j-1][1]

for i in dp:
  print(i)
