def bubble_sort(a, n):
  for i in range(n-1, 0, -1):
    j = i
    while (j < n) and (a[j][1] < a[j-1][1]):
      tmp = a[j-1]
      a[j-1] =  a[j]
      a[j] = tmp
      j += 1
  return a

def selection_sort(a, n):
  for i in range(n):
    minj = i
    for j in range(i, n):
      if a[j][1] < a[minj][1]:
        minj = j
    if i != minj:
      a[minj], a[i] = a[i], a[minj]
  return a

n = int(input())
input1 = input().split()
a = list(input1)
b = a[:]
a = bubble_sort(a, n)
b = selection_sort(b, n)


#*をつけることでタプル（の中に入れた型）として実行が可能になる　タプルはオブジェクトの変更ができない
print(*a)
print("Stable")
print(*b)

if a == b:
  print("Stable")
else:
  print("Not stable")


#a = b[:]とは何か：リストのindexとobjectをまんまコピー
#print(*aとは) タプルとして出力
