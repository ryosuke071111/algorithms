with open('program.txt') as f:
  a = f.read().split("\n")
  flag1=0
  tmp=""
  for i in a:
    if tmp==i and flag1==0:
      print(i)
      flag1=1
    elif tmp==i and flag1==1:
      pass
    else:
      flag1=0
    tmp=i

#簡単
# f = open("program.txt")
# l = f.readlines()

# p = ''
# c = 1
# for ll in l:
#     if (p == ll and c == 1):
#         print(p)
#         c += 1
#     elif(p != ll):
#         c = 1
#     p = ll
