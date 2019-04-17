n,m=map(int,input().split())
n%=12
m=m*360/60
n=n*(360/12)+m/12

print(min(abs(m-n),360-abs(m-n)))


#間違えたコード
# if m ==0:
#   print(min(abs(30*n),360-abs(30*n)))
#   exit()
# print(min(abs(6*m-((n*30)+(6*m*1/12))),abs(360-abs(6*m-((n*30)+(6*m*1/12))))))


# a, b = (int(i) for i in input().split())
# a = a % 12
# a = (a+b/60)*30
# b *= 6
# s  = abs(a-b)
# if s > 180 : s = 360 - s
# print(s)
