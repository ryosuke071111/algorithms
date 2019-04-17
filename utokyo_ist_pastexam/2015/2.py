with open('program.txt') as f:
  a = f.read().split("\n")
  for k,i in enumerate(a):
    print(k,i.strip(';'))


#答え
# f = open("program.txt")
# l = f.readlines()

# for i,ll in enumerate(l):
#     print(i,ll.strip('\n'))
