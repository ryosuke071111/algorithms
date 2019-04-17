n,k=map(int,input().split())
A=list(map(int,input().split()))
ans=0
tmp=sum(A[0:k])
ans=sum(A[0:k])
for i in range(1,len(A)-k+1):
  tmp=tmp-A[i-1]+A[i+k-1]
  ans+=tmp
print(ans)


# 7 4
# 1 2 3 4 5 6

# 7 5
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

#2012- 埼玉県立越谷北高等学科　卒業
#2016- 立教大学経営学部　卒業
#2021- 東京大学情報理工学研究科　修士課程卒業
#2024- 東京大学情報理工学研究科　博士課程卒業
