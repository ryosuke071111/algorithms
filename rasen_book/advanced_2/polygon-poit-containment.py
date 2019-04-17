def dot(a, b):
    return a.real * b.real + a.imag * b.imag


def cross(a, b):
    return a.real * b.imag - a.imag * b.real


n = int(input())
vertices = [complex(*map(int, input().split())) for _ in range(n)]
edges = [(p0, p1) for p0, p1 in zip(vertices, vertices[1:] + [vertices[0]])]

q = int(input())
while q:
    q -= 1
    p = complex(*map(int, input().split()))
    counter = 0
    for p0, p1 in edges:
        a, b = p0 - p, p1 - p
        if a.imag > b.imag:
            a, b = b, a
        crs = cross(a, b)
        if a.imag <= 0 and 0 < b.imag and crs < 0:
            counter += 1
        if crs == 0 and dot(a, b) <= 0:
            print(1)
            break
    else:
        print(2 if counter % 2 else 0)




#一言：与えられた点が、あらかじめ作成した多角形に内包されるか
#処理の流れ：与えられた点を正の方向に伸ばし多角形と交差する回数で判定：
#（多角形線分上判定）点pから、多角形を作る線分の二つの座標からベクトルa,bを作成→ベクトルが同一直線上にあればtrue。（->外積0、内積0以下）
#（交差判定）①a,bの外積が正で、a,bがpからの半直正をまたいで異なる側になる時交差している
#②（内包関係判断）交差回数が奇数：内包、偶数：非内包
