def heapsort(list):
    list_size = len(list) -1
    for i in range((list_size//2), -1, -1): #(二分木なので親ノードのインデックスは(n - 1) / 2 となる、木の最後、遡る）#後半以降の配列の中身を操作する
        sift_down(list, i , list_size) #iの初期値は6

    for i in range(list_size, 0, -1):       #ヒープソート実行。値を昇順にする（最下部から上に遡るイメージで。）　＃最大値を一番後ろに移動させる
        if list[0]>list[i]:
            tmp = list[0]
            list[0]=list[i]
            list[i] = tmp                   #ルートのが最下部よりでかかったらルートと最下部を交換する
            print(list)
            sift_down(list, 0, i-1)
    return list

def sift_down(list, root, bottom): #最大値をルートに持ってくる
    left = root * 2 + 1
    right= root * 2 + 2

    if left <= bottom and list[left] > list[root]:           #左より最下部のがでかい、かつ、左のがルートよりでかい
        max_child = left                                    #マックスチャイルドは左→入れ替える必要あり
    else:
        max_child = root                                    #そうじゃなかったらマックスチャイルドはルート
    if right <= bottom and list[right] > list[max_child]:   #右より最下部のがでかい、かつ、右のがマックスチャイルドよりでかい場合は右をマックスチャイルドに（ルートと右子を比較してる）
        max_child = right

    if max_child != root:                                   #マックスチャイルドがルートじゃなかったら（左とか右だったら）
        list[root], list[max_child] = list[max_child], list[root]   #マックスチャイルドがルートじゃなかったら（左とか右だったら）ルートを変更
        sift_down(list, max_child, bottom)                  #変更かける

if __name__ == '__main__':
    l = [4, 100, 1, 5, 400,53, 54, 53432,5678, 13, 65, 6, 0, 32]
    print('Unsorted')
    print (l)
    print ('Sorted')
    a = heapsort(l)
    print(a)
