
#①
s=input()
st=[]
ans=0
for i in s:
  # print("入力:",i,"stack:",st)
  if i=="0":
    if not st or st[-1]=="0":
      st.append(i)
    elif st[-1]=="1":
      st.pop()
      ans+=2
  elif i =="1":
    if not st or st[-1]=="1":
      st.append(i)
    elif st[-1]=="0":
      st.pop()
      ans+=2
      # print(" 合体",st)
print(ans)

#②
s=input()
zero_c=s.count('0')
one_c=s.count('1')
print(min(zero_c,one_c)*2)

