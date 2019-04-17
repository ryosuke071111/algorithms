from queue import PriorityQueue

INF = 1<<30
n = int(input())
adj =[[] for i in range(n+1)]
maxx = 10010

def dijkstra():
    global adj
    PQ = PriorityQueue()

    d = [INF for i in range(n)]
    flag = [0 for i in range(n)]

    d[0] = 0
    PQ.put((0, 0))
    while (not PQ.empty()):
        f = PQ.get()
        u = f[1]
        flag[u] = 1

        lens = len(adj[u])
        for j in range(lens):
            v = adj[u][j][0]
            if (flag[v] == 0 and d[v] > d[u] + adj[u][j][1]):
                d[v] = d[u] + adj[u][j][1]
                PQ.put((d[v], v))

    for i in range(n):
        if d[i] == INF:
            print("%d %d"%(i, -1))
        else:
            print("%d %d"%(i, d[i]))

for i in range(n):
    s =[int(x) for x in input().split()]
    u = s[0]
    k = s[1]
    for j in range(k):
        adj[u].append((s[j*2+2],s[2*j+3]))

dijkstra()
