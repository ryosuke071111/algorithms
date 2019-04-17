def counting_sort(a,b,k):
  c = [0 for _ in range(k+1)]
  print("0~k+1の出現頻度の箱を初期化",c)
  for i in range(len(a)):
    c[a[i]] += 1
  print("0~k+1の出現頻度の箱に出現頻度を代入する",c)
  for i in range(1, len(c)):
    c[i] += c[i-1]
  print("累積和",c)
  for i in range(len(a) - 1, -1, -1):
    b[c[a[i]]- 1] = a[i]
    c[a[i]] -= 1
  print("bの箱にcの箱の累積和の大きいものの和のインデックスを入れていく",b)

n = int(input())
a = list(map(int, input().split()))
b = [0 for _ in range(len(a))]
counting_sort(a, b, max(a))
print(*b)

