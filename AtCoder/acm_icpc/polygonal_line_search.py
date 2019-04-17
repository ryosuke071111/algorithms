while 1:
  n=int(input())
  if n==0:
    break
  data=[[] for i in range(n+1)]
  for i in range(n+1):
    m=int(input())
    x,y=map(int,input().split())
    for j in range(m-1):
      _x,_y=map(int,input().split())
      data[i].append((abs(_x+_y-x-y),1 if x<_x else 3 if x>_x else 0 if y< _y else 2 ))
      print(data)
      x,y=_x,_y
  for i in range(1,n+1):
    d=[(e[0], (e[1]+(data[0][0][1]-data[i][0][1]))%4) for e in data[i]]
    print(d)
    f=[(e[0], (e[1]+(data[0][0][1]-data[i][-1][1]))%4) for e in data[i][::-1]]
    if data[0]==d:
      print(i)
    elif data[0]==f:
      print(i)
  print('+++++')


