# def chnked(arr,n):
#   return[arr[i:i+n] for i in range(0,len(arr),n)]
# area = chnked(area,2)

x1,y1,x2,y2 = map(int,input().split())
d_x,d_y = x2-x1, y2-y1

x3 = x2-d_y
y3 = y2+d_x
x4 = x1-d_y
y4 = y1+d_x

print(x3,y3,x4,y4)
#yの差をxから引く
#xの差をyにたす
