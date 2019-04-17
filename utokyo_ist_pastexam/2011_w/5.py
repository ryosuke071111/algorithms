from uti import *
f1=open('c1.txt')
f1=f1.read().strip('\n')
f2=open('c2.txt')
f2=f2.read().strip('\n')
print("展開後:",decompression(f1),"展開後文字数:",len(decompression(f1)),decompression(f1)[-10:])
print("展開後:",decompression(f2),"展開後文字数:",len(decompression(f2)),decompression(f2)[-10:])
print("展開後:",decompression("ab000000ab"))
