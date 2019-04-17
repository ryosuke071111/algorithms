s1=open('s1.txt')
s1=s1.read().strip('\n')
s1="aabbccddaabbccddbbccddaa"
# s1="vwabcdefxy002st"

i=0
dic={}
s2=s1

# 辞書作成
while i+5<=len(s1):
  try:
    if len(s1[i:i+6])==6 and s1[i:i+6] not in dic:
      dic[s1[i:i+6]]=str(i).zfill(3)
      fist_half=s2[:i+2]
      second_half=s2[i+2:]
      while s1[i:i+6] in second_half:
          second_half=second_half.replace(s2[i:i+6],dic[s1[i:i+6]])
      s2=fist_half+second_half
    i+=1
  except KeyError:
    pass
  except IndexError:
    break


# print("圧縮文字の長さは",len(s2))
# print("圧縮文字の末尾10文字は",s2[-1:-11:-1])

