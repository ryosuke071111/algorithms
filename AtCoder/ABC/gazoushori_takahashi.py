H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
preS, reS = [["" for _ in range(W)] for _ in range(H)], [["" for _ in range(W)] for _ in range(H)]

def round(i, j):
    rounds = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    search = []
    for r in rounds:
        if 0<= i+r[0] <= H-1 and 0 <= j+r[1]<=W-1:
            search.append([i+r[0], j+r[1]])
    return search

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            preS[i][j] = "."
            for r in round(i, j):
                preS[r[0]][r[1]] = "."

ans = []
for i in range(H):
    out = ""
    for j in range(W):
        if preS[i][j] == "":
            preS[i][j],reS[i][j] = "#",  "#"
            for r in round(i, j):
                reS[r[0]][r[1]] = "#"
        out += preS[i][j]
    ans.append(out)

for i in range(H):
    for j in range(W):
        if not reS[i][j]:
            reS[i][j] = "."

if reS == S:
    print("possible")
    for i in range(H):
        print(ans[i])
else:
    print("impossible")
