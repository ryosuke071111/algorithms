# f = open('program.txt')
# t = f.readlines()
# n = 0

# for c in t:
#   if c ==';':
#     n+= 1
# print(n)

# i=1
# for i,c in enumerate(t):
#   print(i,c.strip('\n'))
#   i +=1

# f = open('program.txt')
# t = f.readlines()

# for i in range(len(t)):
#   if t[i-1] == t[i]:
#     print(t[i].strip('\n'))

# count = 0
# for i in range(len(t)):
#   if t[i]  in t[i+1:]:
#     print(t[i].strip('\n'))
#     count += 1

# print(count)

# f = open('program.txt')
# t = f.read().split('\n')


# def similarity(s1,s2):
#   count = 0
#   length = max(len(s1),len(s2))
#   s1 = s1 + ' ' *(length-len(s1))
#   s2 = s2 + ' ' *(length-len(s2))
#   for i in range(length):
#     if s1[i] != s2[i]:
#       count += 1
#     return count

# ll = []
# c =0
# for l in t:
#   if (len(l) >= 2 and l not in ll):
#     ll.append(l)
# for i in range(len(ll)):
#   for j in range(1, len(ll)):
#     if 0 < similarity(ll[i],ll[j]) <5:
#       print(ll[i])
#       print(ll[j])
#       c += 1
# print(c)

def s(s1,s2):
    t = {}
    for i in range(len(s1)+1):
        t[i,0] = i
    for i in range(len(s2)+1):
        t[0,i] = i
    for i in range(1,len(s1) + 1):
        for j in range(1,len(s2) + 1):
            if (s1[i-1]  == s2[j-1]):
                d = 0
            else:
                d = 1

            t[i,j] = min(t[i,j-1]+1,t[i-1,j]+1,t[i-1,j-1]+d)
            print("t[i,j]:",t[i,j])
            print('t:',t)
            print('i,j:',i,j)
            print('len(s1),len(s2):',len(s1),len(s2))
            print("s1:",s1,"s2:",s2,"\n")
    return t[len(s1),len(s2)]

f = open("program.txt")
l = f.read().split('\n')
ll = []
for lll in l:
    if (len(lll) >=0 and lll not in ll):
        ll.append(lll)
row = len(ll)
for i in range(row):
    for j in range(i+1,row):
        if (s(ll[i],ll[j]) < 5 and s(ll[i],ll[j]) != 0):
            print(ll[i],ll[j],sep=',')
