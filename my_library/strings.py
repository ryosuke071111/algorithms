#数値と文字列の結合
s1 = 'aaa'
s2 = 'bbb'

i = 100
f = 0.25

s = s1 + '_'+format(i,'05')+'_'+s2+'_'+format(f,'.5f')
print(s)


#---------------文字列結合（リストの中身が””内の文字列で結合される）---------------
l = ['aaa', 'bbb', 'ccc']

print('&'.join(l))

s = "aaa\nbbb\ncccc"
s = s.replace('\n',"")
print(s)

#---------------文字列中に改行いれてスペース加える-------------
s = "line1\n"\
    "    line2\n"\
    "       line3\n"
print(s)

s = ("line1\n"
     "   line2\n"
     "      line3")

print(s)

s = "aaa"
r = "bbbb"
print(s,end="")
print(r)

#--------------------長い文字列を複数行に分けて書く-----------
s = ('https://ja.wikipedia.org/wiki/\n'
     '%E3%83%97%E3%83%AD%E3%82%B0%E3%83\n'
     '%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E\n')
print(s,end="")

#--------------------正規表現------------------------
s = s.replace('\n',"")
import re
post = "124567aaaaaaaaaaa"
a = re.match("125{3}",post)
print(a.group())
#-------------------正規表現で置換------------------
s = input()
print(re.sub("B+","B",s))


#------------------文字列削除-----------------
s = input()
string=[]
for i in s:
  if i == "B" and len(string)>0:
    del string[-1] #ここ！
  elif i == "1" or i == "0":
    string.append(i)
print("".join(string))
