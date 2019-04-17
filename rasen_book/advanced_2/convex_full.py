def cross(a, b):
  return a.real * b.imag - a.imag * b.real

def dot(a, b):
  return a.real * b.real + a.imag * b.imag

def convex_hull(p):
  pp = sorted(p, key=lambda x:(x.imag, x.real))  #y座標を優先して昇順、同じならxで昇順
  n = len(pp)
  ans, j = [0] * (n+1), 0
  for i in range(n):
    while j > 1 and cross(ans[j-1]-ans[j-2], pp[i]-ans[j-1]) < 0: #今の線分と1つ前の線分の成す角が90度越える時
      j -= 1
    ans[j] = pp[i]
    j += 1
  k = j #上前半をkで固定している
  for i in range(n-2, -1, -1):
    while j > k and cross(ans[j-1]-ans[j-2], pp[i]-ans[j-1]) < 0:
      j -= 1
    ans[j] = pp[i]
    j += 1
  print('ans is', ans)
  print('pp is', pp)
  return ans[0:j-1]

n = int(input())
p = []
for i in range(n):
  x, y = list(map(int, input().split()))
  p.append(complex(x, y))
ans = convex_hull(p)
print(len(ans))
for i in ans:
  print(int(i.real), int(i.imag))

#一言：与えられた点を囲む点の座標の出力
#処理の流れ：アンドリューのアルゴリズム
#①所与の点をxについて昇順整列→②Uに小さい順にappend→③Lに大きい順にappend
#計算量：O(nlogn)凸包生成：O(n)* 整列：O(logn)
