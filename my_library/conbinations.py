import math
import itertools

#------------------順列----------------------------------

#順列。重複組合せば別のものとする。4!の場合4つ並べる。4*3の場合4つの中から2つ
l = ['a', 'b', 'c', 'd']
# count = 0
# for i in itertools.permutations(l,3):
#   print(i)
#   count += 1
# print(count)

# l_list = list(itertools.permutations(l,3))


#-----------------組み合わせ----------------------------------
#組み合わせ。重複なし。
def combinations(n,r):
  return math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
print(combinations(10,2))

def combination_with_replacement(n,r):
  return combinations(n+r-1,r)
print(combination_with_replacement(10,2))

#組み合わせ列挙
for i in itertools.combinations(l,2):
  print(i)

#重複組合せ
for i in itertools.combinations_with_replacement(l,2):
  print(i)

#文字列を並び替えて文字を作る
s='atcoder'
for i in itertools.combinations_with_replacement(s,len(s)):
  print(i)
