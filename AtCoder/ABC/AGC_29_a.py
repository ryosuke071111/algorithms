# from bisect import bisect_left
s=list(input())
count=0
# print('lens',len(s))
indexes = [i for i, x in enumerate(s) if x == "B"]
ideal=sorted([len(s)-i-1 for i in range(len(indexes))])
# print(indexes)
# print(ideal)
for i in range(len(indexes)):
  count+=ideal[i]-indexes[i]

print(count)


