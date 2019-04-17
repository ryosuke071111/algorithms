s = input()
k = int(input())

#正解(全列挙してソートしてる)
sub_string=[]
for i in range(len(s)):
  for j in range(1,k+1):
    sub_string.append(s[i:i+j])
sub_string=list(set(sub_string))
sub_string.sort()
print(sub_string[k-1])


# #自分の間違った回答
# a = min(s)
# if k == 1:
#   print(a)
#   exit()

# indexes = [i for i, x in enumerate(s) if x == a]

# b='z'*5001

# for i in indexes:
#   if i + 1 < len(s):
#     if s[i]+s[i+1] < b:
#       b = s[i]+s[i+1]
#       index = i
# if k == 2:
#   print(b)
#   exit()

# if len(s) < k:
#   a=min([i for i in s if i != a])
#   print(s[s.index(a):k-len(s)+1])
#   exit()
# elif len(s[index:index+k]) < k:
#   a=min([i for i in s if i != a])
#   print(s[s.index(a)]+(s[index:index+(k-len(s[index:index+k]))-1]))
# else:
#   print(s[index:index+k])



