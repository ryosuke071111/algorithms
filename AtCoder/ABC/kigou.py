# from collections import deque
# o = deque(input())
# e = deque(input())

# output = []

# while len(o) >0 and len(e) >0:
#   output.append(o.popleft())
#   output.append(e.popleft())

# if len(o) !=0:
#   output.append(o.popleft())
# elif len(e) !=0:
#   output.append(e.popleft())
# else:
#   pass

# print("".join(output))


from collections import Counter
n = int(input())
v = list(map(int, input().split()))
a = Counter(v[::2]).most_common()
b = Counter(v[1::2]).most_common()

if len(a) ==1:
  a.append([0,0])
if len(b) == 1:
  b.append([0,0])
print(a)
print(b)

#お互いの最頻値が同じ値なら
if a[0][0] == b[0][0]:
  #まず最頻値に合わせる、そして、次に多いものに合わせる
  if a[1][1]>b[1][1]:
    print(n-a[1][1] - b[0][1])
  else:
    print(n-a[0][1]-b[1][1])

#お互いのセットの最大値が違う数字なら
#互いのセットの最頻値を引く（=最頻値でないものをリプレイス）
else:
  print(n-a[0][1]-b[0][1])
