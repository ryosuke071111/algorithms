# a,b,x=map(int,input().split())
# print(b//x-(a-1)//x)
# print("".join(list(map(lambda x:x[0],list(input().split())))))
# ls=[input() for i in range(3)]
# print(ls[0][0]+ls[1][1]+ls[2][2])
# a,b,c=map(int,input().split())
# print('Yes' if a+b>=c else "No")
# n=int(input())
# a=int(input())
# print('Yes' if n%500<=a else "No")
# s=input()
# print(700+s.count('o')*100)
# n,m=map(int,input().split())
# ls=[0]*m
# for i in range(n):
#   A=list(map(int,input().split()))[1:]
#   for j in A:
#     ls[j-1]+=1
# print(sum(list(map(lambda x:x//n,ls))))

a,b,c=map(int,input().split())
k=int(input())
print(sum(sorted([a,b,c])[:2])+(max(a,b,c)*(2**k)))

# 6 12 24
