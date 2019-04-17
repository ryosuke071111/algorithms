TARGET = 3797645

NUM = 1000000000000000000 # 1億個
list = range(NUM) # [0, 1, 2...]

low = 0
high = len(list)
while (low != high): # 検索したい値が存在しない場合は終了
    center = (low + high) // 2
    print(center)
    if (list[center] < TARGET): #真ん中の値がターゲットより小さかったら
        low = center + 1        #lowを真ん中+1
        print(low)
    elif (TARGET < list[center]):#真ん中の値がターゲットより大きかったら
        high = center - 1       #highを真ん中-1
    else:                       #一致したら終わり
        break # 検索したい値が見つかった
