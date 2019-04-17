f1=open('c1.txt')
f2=open('c2.txt')
f1=f1.read().strip('\n')
f2=f2.read().strip('\n')
alphabet = [chr(ord('a') + i) for i in range(26)]+[" ",".",","]
count1=0
count2=0
for i in f1:
  if i not in alphabet:
    count1+=1
for i in f2:
  if i not in alphabet:
    count2+=1
print(count1//3)
print(count2//3)
