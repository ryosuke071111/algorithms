# ##ケース①
# maxv = 0
# list1 =[]

# #配列の入力に数字しか受け入れない
# #「終わり」の文字列が来た場合にのみ対処する
# while True:
#   try:
#     a = input()
#     b = int(a)
#     list1.append(b)
#   except ValueError:
#     if a == "終わり":
#       break
#     else:
#       print('数字を入力してください')
#       continue
# print(list1)

# #比較する
# minv = list1[0]
# for j in range(len(list1)):
#   maxv = max(maxv, list1[j]-(minv))
#   minv = min(minv, list1[j])
# print(maxv)


##ケース②
#最初のnの数だけ成分を作っていく
n = int(input())
R = [int(input()) for i in range(n)]

minv = R[0]
maxv = R[1] - R[0]
for j in range(1, n):
  if (maxv < R[j] - minv):
    maxv = R[j] - minv
  if (R[j] < minv):
    minv = R[j]
print(maxv)
