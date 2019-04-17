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
    if dp[len(a)][len(b)] < 4:
      return True

pairs=[]
f=open('program.txt')
a=f.read().split('\n')[:-1]
a=sorted(set(list(map(lambda x:x.strip(';'),a))))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if judge(a[i],a[j]):
          pairs.append([a[i],a[j]])

for i in pairs:
    print(i[0],",",i[1])



# def s(s1,s2):
#     t = {}
#     for i in range(len(s1)+1):
#         t[i,0] = i
#     for i in range(len(s2)+1):
#         t[0,i] = i
#     for i in range(1,len(s1) + 1):
#         for j in range(1,len(s2) + 1):
#             if (s1[i-1]  == s2[j-1]):
#                 d = 0
#             else:
#                 d = 1
#             t[i,j] = min(t[i,j-1]+1,t[i-1,j]+1,t[i-1,j-1]+d)
#     return t[len(s1),len(s2)]

# f = open("program.txt")
# l = f.read().split('\n')
# ll=sorted(set(l))
# row = len(ll)
# for i in range(row):
#     # n*nの組み合わせの道のパターンの組み合わせはiの時,[i+1]:で出せる
#     for j in range(i+1,row):
#         if (s(ll[i],ll[j]) < 4 and s(ll[i],ll[j]) != 0):
#             print(ll[i],ll[j],sep=',')


