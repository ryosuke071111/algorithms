d,n = map(int,input().split())

if n != 100:
  print((100**d)*n)
else:
  print((100**d)*(n+1))

#10000から始まる場合はそれが1番目だから100番目は1010000
