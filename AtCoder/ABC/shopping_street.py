# N = int(input())
# F = [list(map(int,input().split())) for i in range(N)]
# P = [list(map(int,input().split())) for i in range(N)]

# ans = -float('inf')
# for k in range(1,1<<10):
#     tmp = 0
#     for fs,ps in zip(F,P):
#         cnt = 0
#         for b in range(10):
#             if (k>>b)&1 and fs[b]:
#                 cnt += 1
#         tmp += ps[cnt]

#     ans = max(ans, tmp)
# print(ans)

N = int(input())
F = [list(map(int,input().split())) for i in range(N)]
P = [list(map(int,input().split())) for i in range(N)]

ans = -float('inf')
for k in range(1,1<<10):
    tmp = 0
    for fs,ps in zip(F,P):
        cnt = 0
        for b in range(10):
            if (k>>b)&1 and fs[b]:
                cnt += 1
        tmp += ps[cnt]
    ans = max(ans, tmp)
print(ans)

