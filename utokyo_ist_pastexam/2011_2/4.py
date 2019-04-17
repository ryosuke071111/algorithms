f1=open('s1.txt')
f1=f1.read().strip('\n')
f2=open('s2.txt')
f2=f2.read().strip('\n')
def make_dic(f):
  dic={}
  i=0
  while i <len(f)-5:
    if f[i:i+6] not in dic:
      dic[f[i:i+6]]="0"*(3-len(str(i)))+str(i)
    else:
      pass
    i+=1
  return dic
def compression(f):
  dic= make_dic(f)
  i=0
  ans=""
  while i < len(f):
    if f[i:i+6] in dic and int(dic[f[i:i+6]])!=i:
      ans+=dic[f[i:i+6]]
      i+=5
    else:
      ans+=f[i]
    i+=1
  return ans
print(compression(f1))
print(compression(f2))

# 答え照合
# def make_dic(s):
#     dic = {}
#     i = 0
#     while i+6 < len(s):
#         if s[i:i+6] not in dic:
#             val = str(i)
#             while len(val) < 3:
#                 val = "0" + val
#             dic[s[i:i+6]] = val
#         i += 1
#     return dic

# def compress_str(s):
#     dic = make_dic(s)
#     print(dic)
#     s_ans = str()
#     i = 0
#     while i < len(s):
#         substr = s[i:i+6]
#         if substr in dic and int(dic[substr]) != i:
#             s_ans += dic[substr]
#             i += 6
#         else:
#             s_ans += s[i]
#             i += 1
#     return s_ans

# with open("s1.txt", "r") as strFile:
#     s = strFile.read()
#     print ("compressed string of s1.txt is \"{}\"".format(compress_str("aabbbaaabbbacabbbaabbbacaa")))

# with open("s2.txt", "r") as strFile:
#     s = strFile.read()
#     print ("compressed string of s2.txt is \"{}\"".format(compress_str(s)))
