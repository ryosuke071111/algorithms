list1= list(map(int,input().split()))
list1.sort()
print(abs(list1[0]-list1[1])+abs(list1[1]-list1[2]))
