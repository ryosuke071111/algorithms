#8:54
import itertools

logic=input()
alphabet=set([])
kigou=["&","+"]

for i in logic:
  if i not in kigou and i not in alphabet:
    alphabet.add(i)

alphabet=list(alphabet)

ans=[]

for i in itertools.product(range(2),repeat=len(alphabet)):
  for j in range(len(alphabet)):
    if "!" in logic:
      logic=logic.replace("!",abs(-1+))
  if eval(logic)==True:
    ans.append(i)

print(abs(-1+1)&0&abs(-1+1)+0)
