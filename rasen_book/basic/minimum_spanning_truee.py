n = int(input())
a =[]

for i in range(n):
    inp = input()
    if "-1" in inp:
        inp = inp.replace("-1", "10000")
    a.append(list(map(int, inp.split())))

w = 0
v = set()
v.add(0)

while len(v) < n:
    min_w = 10000
    min_idx = 0
    i = 0
    for node in v:
        if min_w > min(a[node]):
            min_w = min(a[node])
            i = node
            min_idx = a[i].index(min_w)
            print('min_w is',min_w)
            print('min_idx is',min_idx)
    if min_idx in v:
        a[i][min_idx] = 10000
        continue
    else:
        w += min_w
        v.add(min_idx)
    print("a is", a)
print(w)
