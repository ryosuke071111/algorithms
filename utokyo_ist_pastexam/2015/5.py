def judge(a,b):
    if a==b:
        return False
    length=max(len(a),len(b))
    a+=" "*(length-len(a))
    b+=" "*(length-len(b))
    i=0
    cnt=0
    while i < len(a):
        if a[i]!=b[i]:
            cnt+=1
        if cnt>=5:
            return False
        i+=1
    return True

pairs=[]
f=open('program.txt')
a=f.read().split('\n')[:-1]
a=sorted(set(list(map(lambda x:x.strip(';'),a))))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if judge(a[i],a[j]):
          pairs.append([a[i],a[j]])

for i in pairs:
    print(i[0],",",i[1])
print(len(pairs))





# def s(s1,s2):
#     l = max(len(s1),len(s2))
#     ss1 = s1 + ' ' * (l - len(s1))
#     ss2 = s2 + ' ' * (l - len(s2))
#     c = 0
#     for i in range(l):
#         if (ss1[i] != ss2[i]):
#             c += 1
#     return c

# f = open("program.txt")
# l = f.read().split('\n')
# ll = []
# for lll in l:
#     if ( lll not in ll):
#         ll.append(lll)
# row = len(ll)
# for i in range(row):
#     for j in range(i+1,row):
#         if (s(ll[i],ll[j]) < 5 and s(ll[i],ll[j]) != 0):
#             print(ll[i],ll[j],sep=',')
