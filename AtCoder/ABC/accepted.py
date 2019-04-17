s=input()
if "C" in s[2:-1] and s[0]=="A":
  a=s[1]+s[2:-1].replace('C',"",1)+s[-1:]
  if a == a.lower():
    print("AC")
  else:
    print('WA')
    exit()
else:
  print('WA')
