with open('program.txt') as f:
  a=f.read().split('\n')
  count=0
  for i in a:
    for j in i:
      count+=j.count(';')
  print(count)


#答え
# f = open("program.txt")
# t = f.read()

# n = 0
# for c in t:
#     if (c == ';'):
#         n += 1

# print (n)

