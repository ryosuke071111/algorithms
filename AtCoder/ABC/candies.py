n = int(input())
area = [list(map(int,input().split())) for i in range(2)]

max_v=0

for i in range(n):
  max_v = max(max_v,sum(area[0][0:i+1])+sum(area[1][i:n]))


print(max_v)

#惜しい。0:i,i+nをとるところまではできていた。
#が、上下の配列の最大の差をとってそのiの部分で区切って前後の配列を足し合わせるという複雑なことをしていた。＝シンプルに考えて良い。
