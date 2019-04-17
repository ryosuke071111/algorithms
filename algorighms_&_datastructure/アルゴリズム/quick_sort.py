x = [4, 1, 1, 5, 400,53, 54, 53432,5678, 13, 65, 6, 0, 32]

def quick_sort(arr):
    left = []
    right = []
    if len(arr)<=1:     #配列の大きさが1以下なら
        return arr      #配列をそのまま返す
    ref = arr[1]        #配列の0番目をrefに代入する
    ref_count = 0       #refc_countを0にする
    # print(ref)
    for ele in arr:     #配列の中でeleをどのドン増やしていく
        if ele < ref:   #refよりeleが小さい場合
            left.append(ele)    #左にeleをappendする
            # print(left)
            # print('↑左☆')
        elif ele > ref:         #eleのがrefより大きい場合
            right.append(ele)      #rightにappendmする
            # print(right)
            # print('↑右★')
        else:
            ref_count += 1      #それ以外はref_countを増やす
    left = quick_sort(left)        #配列のappendが終わったらleftのクイックソートをする
    right = quick_sort(right)      #配列のappendが終わったらrightのクイックソートをする
    # print(left)
    # print('左終わりい')
    # print(right)
    # print('右終わりいい')
    print(left + [ref] * ref_count + right)
    return left + [ref] * ref_count + right


x = quick_sort(x)
print(x)
