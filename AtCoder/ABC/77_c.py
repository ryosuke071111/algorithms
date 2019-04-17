from bisect import bisect_left,bisect_right
n=int(input())
A=sorted(list(map(int,input().split())))
B=sorted(list(map(int,input().split())))
C=sorted(list(map(int,input().split())))

ans=0

for i in B:
  sml_B = bisect_left(A,i)
  # print(i,"sml_B",sml_B)
  big_B = len(C)-bisect_right(C,i)
  # print(i,"big_B",big_B)
  ans+=sml_B*big_B
print(ans)
