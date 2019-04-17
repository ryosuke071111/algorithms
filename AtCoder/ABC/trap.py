w=input()
list=["a","i","u","e","o"]
for i in w:
  if i in list:
    w = w.replace(i,"")
print(w)
