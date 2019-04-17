h,w = map(int,input().split())
area = [input() for i in range(h)]

for i in range(h):
  for j in range(w):
    count = 0
    if area[i][j] == ".":
      for s in range(-1,2):
        for t in range(-1,2):
          if 0 <= i + s <h and 0 <= j+t < w:
            if area[i+s][j+t] == '#':
              count += 1
          else:
            continue
      print(count, end='')
    else:
      print("#", end='')
  print()





