#1
a,b,c,x,y=map(int,input().split())
print(min(x*a+y*b,2*x*c+b*max(0,y-x),2*y*c+a*max(0,x-y)))

#2
# a,b,c,x,y = map(int, input().split())
# mx = a if x >= y else b
# if c * 2 <= (a+b):
#   if c * 2 <= mx:
#     print((min(x,y)+abs(x-y))*c*2)
#   else:
#     print(min(x,y)*c*2+abs(x-y)*mx)
# else:
#   print(a*x+b*y)



#ある何かで一気に引くときは小さい方をとって掛ける
#その次に、余りを大きい方-小さい方で出して、その数で掛けるのか、単体の金額で掛けるのかを大小で判別
