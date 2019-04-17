import re
s="chokudaiatcoder"

#sの中に[a-z]が連続して2つあったらそれを"置換"に置換
a=re.sub("[a-z]{2}","置換",s)
print(a)

#先頭の[a-z]（該当条件）のみ"置換"に置換
a=re.sub("^[a-z]","置換",s)
print(a)

#"aiueo"に該当する文字の中から3つ連続しているものがあれば置換
a=re.sub("[aiueo]{3}","置換",s)
print(a)

a=re.sub("tco+","置換",s)
print(a)


content = '(hellow) pythonpythonpython, 123, end,1932. 1112'
result= re.search("py..on",content) #任意の.文字
result= re.search("(py..on)+",content) #単語の繰り返しはカッコでくくって+
result= re.search("(py..on){2}",content) #単語の繰り返しに回数指定が欲しい場合は番号入れる
result= re.search("py.*",content) #それに該当する文字列以降を全て抽出
result= re.search("(py..on){2}",content) #単語の繰り返しに回数指定が欲しい場合は番号入れる
result= content.startswith("(")
result= re.findall("[0-9]+",content) #該当するものを全部
result= re.find("[0-9]+",content)
print(result)
