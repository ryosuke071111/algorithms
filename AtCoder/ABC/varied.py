#自分のコード
# from collections import Counter
# s=Counter(input()).most_common()
# for _,i in s:
#   if i !=1:
#     print('no')
#     exit()
# print('yes')

#人のコード
s=input()
if len(s) ==len(set(s)):
  print('yes')
else:
  print('no')
