n = int(input())

36
52
99

187

25
44

i+1にC秒で向かう

iからi+1には複数の列車が発車するけど開始s秒後にiを発車し、そのあとはf秒おきにiを発車
sはfで割り切れる

つまり、s<=t, t%f == 0 を満たすtに対してのみ開始t秒後に駅iを出発し、t+C秒後にi+1駅に到着する列車がある

全ての駅iに対してiからnに到着できる時間を答える


1, c,s,f
2, c,s,f

36+4+52 =92+