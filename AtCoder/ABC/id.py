import bisect

n,m = map(int,input().split())
years = [[]for i in range(n)]
yearss = []


for i in range(m):
  p,y = map(int,input().split())
  years[p-1].append(y)
  yearss.append([p,y])


for i in range(n):
  years[i].sort()

for i in range(m):
  print("{0:06d}".format(yearss[i][0]),"{0:06d}".format(bisect.bisect_right(years[yearss[i][0]-1],yearss[i][1])),sep="")

#別解
# I=lambda:list(map(int,input().split()[::-1]))
# m,n=I()
# c=[0]*-~n
# a=[0]*m
# for y,p,i in sorted(I()+[i]for i in range(m)):
#   c[p]+=1
#   a[i]='%06d%06d'%(p,c[p])
# print(a)
