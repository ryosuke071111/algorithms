#10:10
n=int(input())
A=list(map(int,input().split()))
A=list(map(lambda x:x//400 if x//400<=7 else 8 ,A))
target=A.count(8)
total=len(set(A))
min=total-1 if 8 in A else total
print(min if min!=0 else 1,min+target)

#場合分けを気をつける
