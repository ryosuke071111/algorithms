def s(s1,s2):
    t = {}
    for i in range(len(s1)+1):
        t[i,0] = i
    for i in range(len(s2)+1):
        t[0,i] = i
    for i in range(1,len(s1) + 1):
        for j in range(1,len(s2) + 1):
            if (s1[i-1]  == s2[j-1]):
                d = 0
            else:
                d = 1
            t[i,j] = min(t[i,j-1]+1,t[i-1,j]+1,t[i-1,j-1]+d)
    return t[len(s1),len(s2)]

#配列ver
def judge(a,b):
    if a==b:
        return False
    dp = [[0 for i in range(len(b)+1)]for i in range(len(a)+1)]
    for i in range(len(a)):
      dp[i][0]=i
    for i in range(len(b)):
      dp[0][i]=i
    for i in range(1,len(a) + 1):
        for j in range(1,len(b) + 1):
            if (a[i-1]  == b[j-1]):
                d = 0
            else:
                d = 1
            dp[i][j] += min(dp[i][j-1]+1,dp[i-1][j]+1,dp[i-1][j-1]+d)
    return dp[len(a)][len(b)]

