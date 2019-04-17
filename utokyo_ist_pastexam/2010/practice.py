class Rect(object):
  def __init__(self,x,y,w,h):
    self.x=x
    self.y=y
    self.w=w
    self.h=h
  def set_par(self,par):
    self.par=par

def is_intersect(rec1,rec2):
  x1=rec1.x+float(rec1.w)/2
  y1=rec1.y+float(rec1.h)/2
  x2=rec2.x+float(rec2.w)/2
  y2=rec2.y+float(rec2.h)/2
  actual_dis_x=abs(x1-x2)
  logical_dis_x=float(rec1.w+rec2.w)/2
  actual_dis_y=abs(y1-y2)
  logical_dis_y=float(rec1.h+rec2.h)/2
  if actual_dis_x==logical_dis_x and actual_dis_y == logical_dis_y:
    return False
  elif actual_dis_x <= logical_dis_x and actual_dis_y <= logical_dis_y:
    return True

def find_set(recl,rec):
  if recl[rec.par]==rec:
    return rec
  else:
    return find_set(recl,recl[rec.par])

def union(recl,rec1,rec2):
  x= find_set(recl,rec1)
  y= find_set(recl,rec2)
  if x!=y:
    x.par=y.par
recl=[]

f=open('1000.txt')
for i in f:
  x,y,w,h=map(int,i.split())
  r=Rect(x,y,w,h)
  recl.append(r)
  r.set_par(len(recl)-1)


#厚さ判定
pile=0
area=[[0 for i in range(1000)] for i in range(1000)]
for rec in recl:
  for i in range(rec.x,rec.x+rec.w):
    for j in range(rec.y,rec.y+rec.h):
      area[i][j]+=1
for i in range(1000):
  for j in range(1000):
    pile=max(pile,area[i][j])
print('最大の厚さは',pile)

#クラスターの数
for i in range(len(recl)-1):
  for j in range(i+1,len(recl)):
    rec1=recl[i]
    rec2=recl[j]
    if is_intersect(rec1,rec2):
      union(recl,rec1,rec2)
cluster=0

#親が自身=クラスター数ということ
for rec in recl:
  if find_set(recl,rec)==rec:
    cluster+=1
print('クラスターの数は',cluster)

dic={}

#クラスタの中の要素の数
for rec in recl:
  tmp=find_set(recl,rec)
  if tmp in dic:
    dic[tmp]+=1
  else:
    dic[tmp]=1
print("最大のクラスタの要素数は",max(dic.values()))

#キューは一度初期化してからでないと要素を二ついれられない
#またはカギカッコの中に普通の格好を入れるような形にする
from collections import deque
tmp=0
square=0
xy=[(1,0),(0,-1),(-1,0),(0,1)]
for i in range(1000):
  for j in range(1000):
    if area[i][j]>0:
      que=deque([(i,j)])
      tmp=1
      area[i][j]=0
      while que:
        x,y=que.pop()
        for dx,dy in xy:
          nx,ny=x+dx,y+dy
          if 0<= ny <= 1000 and 0<= nx <= 1000 and area[nx][ny]>0:
            tmp+=1
            area[nx][ny]=0
            que.append((nx,ny))
    square=max(tmp,square)

print('最大のクラスタ内のエリアは',square)









